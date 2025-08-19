import subprocess
import os
import glob

projects = [
    "List-1", "List-2",
    "Logic-1", "Logic-2",
    "String-1", "String-2",
    "Warmup-1", "Warmup-2"
]

def run_pytest_individually(projects):
    passed_projects = 0
    total_projects = 0

    for project in projects:
        project_path = os.path.abspath(project)
        test_dir = os.path.join(project_path, "tests")

        if not os.path.isdir(test_dir):
            print(f"⚠️ Skipping {project}: no tests/ directory found.")
            continue

        # test_*.py を列挙
        test_files = glob.glob(os.path.join(test_dir, "test_*.py"))

        if not test_files:
            print(f"⚠️ No test files in {project}/tests/")
            continue

        print(f"📂 Running tests in {project}/tests...")
        all_passed = True
        for test_file in test_files:
            relative_test_path = os.path.relpath(test_file, project_path)
            result = subprocess.run(
                ["python", "-m", "pytest", relative_test_path, "--tb=no", "--no-header", "--no-summary"],
                cwd=project_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode != 0:
                all_passed = False
                break

        total_projects += 1
        if all_passed:
            passed_projects += 1
            print(f"✅ {project} PASSED")
        else:
            print(f"❌ {project} FAILED")

    print(f"\n✅ Passed Projects: {passed_projects} / {total_projects}")

if __name__ == "__main__":
    run_pytest_individually(projects)
