from prefect import Flow, task
from prefect.schedules import IntervalSchedule
import datetime
import subprocess


# Define a task to run a DVC stage
@task
def run_dvc_stage(stage_name):
    print(f"Running DVC stage: {stage_name}")
    result = subprocess.run(
        ["dvc", "repro", stage_name], capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(f"Error running DVC stage {stage_name}: {result.stderr}")


# Define your Prefect Flow
with Flow("ML Training Pipeline") as flow:
    # Define tasks corresponding to DVC stages
    preprocess_data = run_dvc_stage("preprocess")
    train_model = run_dvc_stage("train")
    evaluate_model = run_dvc_stage("evaluate")

    # Define dependencies (order of execution)
    train_model.set_upstream(preprocess_data)
    evaluate_model.set_upstream(train_model)

# Define a schedule (e.g., run daily)
schedule = IntervalSchedule(interval=datetime.timedelta(days=1))

# Register the flow with the schedule
flow.schedule = schedule

# Run the flow
if __name__ == "__main__":
    flow.run()
