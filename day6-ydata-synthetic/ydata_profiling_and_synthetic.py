from pmlb import fetch_data
from ydata_profiling import ProfileReport
from ydata_synthetic.synthesizers.regular import RegularSynthesizer
from ydata_synthetic.synthesizers import ModelParameters, TrainParameters

# Defining the training and model parameters
batch_size = 500
epochs = 500+1
learning_rate = 2e-4
beta_1 = 0.5
beta_2 = 0.9

# Get data
data = fetch_data('adult')
num_cols = ['age', 'fnlwgt', 'capital-gain', 'capital-loss', 'hours-per-week']
cat_cols = ['workclass','education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'native-country', 'target']

# Profiling report
profile = ProfileReport(data, title="Profiling Report")
profile.to_file("profiling_report.html")

# Generate synthetic data
ctgan_args = ModelParameters(batch_size=batch_size,
                             lr=learning_rate,
                             betas=(beta_1, beta_2))

train_args = TrainParameters(epochs=epochs)

synth = RegularSynthesizer(modelname='ctgan', model_parameters=ctgan_args)

synth.fit(data=data, train_arguments=train_args, num_cols=num_cols, cat_cols=cat_cols)
synth_data = synth.sample(10000)

# Profile synth data
profile_synth = ProfileReport(synth_data, title="Synthetic Data Profiling Report")
profile_synth.to_file("synth_profiling_report.html")
