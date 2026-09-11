## Date
- 11-09-2026

### Time spent
- approx 2.5 hrs

### Concepts learned

- Python environments and package management using Conda
- Project structure and organizing folders by purpose
- VS Code Python interpreter selection and troubleshooting
- Git repository initialization (`git init`)
- Git staging (`git add`)
- Checking repository state (`git status`)
- Viewing commit history (`git log`)
- Creating commits (`git commit`)
- Difference between working directory, staging area, and repository
- Environment specification using `environment.yml`

### Mathematical reasoning understood

- Each project should have its own Python environment so that it can use the required Python version and packages without conflicts with other projects.
- `environment.yml` improves reproducibility by recording the project's required environment and dependencies so the environment can be recreated later.
- Git uses a staging area so we can explicitly choose which changes/files should be included in the next commit.
- Git tracks files rather than empty directories; an empty directory contains nothing for Git to record.
- An algorithm is the core implementation. Experiments involve deliberately changing parameters or conditions to investigate how those changes affect the algorithm's behavior.
- Different algorithms and experiments produce different results, so organizing them into separate folders makes the project easier to understand and maintain.

### Implementation

- Created the initial Machine Learning Research Lab folder structure.
- Initialized the project as a Git repository.
- Created the project `README.md`.
- Created and configured the `ml-lab` Conda environment with Python 3.12, NumPy, and Matplotlib.
- Created `environment.yml` for environment reproducibility.
- Configured VS Code to use the `ml-lab` Python interpreter.
- Troubleshot and fixed the stale VS Code Python interpreter configuration.
- Created two meaningful Git commits:
  - `project started and created README.md`
  - `configure project environment`

### Questions + resolutions

- **Will Git repositories/branches from previous projects interfere with this project?**
  - No. Each project has its own Git repository when initialized in its own folder.

- **Does `git add` automatically stage future edits?**
  - No. Git detects future modifications, but the modified file must be staged again with `git add` before committing.

- **Why use a separate Python environment?**
  - To avoid package/version conflicts between different projects.

- **Why not commit the huge `conda env export` output?**
  - It contains many automatically installed/transitive dependencies and machine-specific details. Our `environment.yml` should communicate the main software requirements needed to recreate the project environment.

- **Why doesn't Git track empty directories?**
  - Git tracks files, so an empty directory has no file for Git to record.

- **Where should `PROGRESS_TRACKING.md` live?**
  - At the project root because it tracks the progress of the entire project.

- **Why separate algorithms, experiments, and results?**
  - The algorithm is the reusable implementation; experiments investigate how the algorithm behaves under different conditions or parameters, and each experiment produces its own results. Organizing them separately keeps the project understandable.

- **What caused the VS Code Python interpreter problem?**
  - A stale global default interpreter path pointed to an old environment. Resetting the Python default interpreter setting removed the stale path, after which `ml-lab` was selected for the project.

### What I can rebuild from memory

- Initialize a Git repository from the project root:
  `git init`

- Create a Conda environment:
  `conda create -n <environment_name> python=3.12`

- Activate the environment:
  `conda activate <environment_name>`

- Install packages:
  `conda install <package1> <package2>`

- Select the Python interpreter in VS Code:
  `Ctrl + Shift + P` → `Python: Select Interpreter`

- Check Git repository state:
  `git status`

- Stage files:
  `git add <file>`

- Create a commit:
  `git commit -m "<message>"`

### Next task

Begin the complete Logistic Regression module:
- Understand the mathematical reasoning and equations.
- Design the algorithm implementation from scratch.
- Decide the required classes/functions, parameters, and return values.
- Implement the training and prediction process.
- Add appropriate metrics.
- Create visualizations to understand model behavior.
- Run experiments to study how parameters affect the algorithm.