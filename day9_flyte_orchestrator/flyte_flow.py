from flytekit import task, workflow
import subprocess


# Define a task to run a DVC stage
@task
def run_dvc_stage(stage_name):
    print(f"Running DVC stage: {stage_name}")
    result = subprocess.run(
        ["dvc", "repro", stage_name], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error running DVC stage {stage_name}: {result.stderr}")


# Define Flyte Flow
@workflow
def ml_training_pipeline() -> None:
    preprocess_data = run_dvc_stage(stage_name="preprocess")
    split_data = run_dvc_stage(stage_name="split")
    train_model = run_dvc_stage(stage_name="train")
    evaluate_model = run_dvc_stage(stage_name="evaluate")
