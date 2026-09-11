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
- Learned the purpose of `.gitignore`.
- Learned how to create a `.gitignore` file and decide which files/folders should be ignored.
- Learned why Python's `__pycache__/` and Jupyter's `.ipynb_checkpoints/` should generally be ignored.
- Learned how to connect a local Git repository to a GitHub repository.
- Learned about Git remotes and the meaning of `origin`.
- Learned how to rename the Git branch from `master` to `main`.
- Learned why `main` is commonly used as the modern/default branch name.
- Learned how to push a local repository to GitHub.
- Learned how upstream tracking works between the local `main` branch and `origin/main`.

### Mathematical reasoning understood

- Each project should have its own Python environment so that it can use the required Python version and packages without conflicts with other projects.
- `environment.yml` improves reproducibility by recording the project's required environment and dependencies so the environment can be recreated later.
- Git uses a staging area so we can explicitly choose which changes/files should be included in the next commit.
- Git tracks files rather than empty directories; an empty directory contains nothing for Git to record.
- An algorithm is the core implementation. Experiments involve deliberately changing parameters or conditions to investigate how those changes affect the algorithm's behavior.
- Different algorithms and experiments produce different results, so organizing them into separate folders makes the project easier to understand and maintain.
- Understood why `__pycache__/` does not need to be tracked: Python can automatically generate it on each local machine.
- Understood why `.ipynb_checkpoints/` does not need to be tracked: Jupyter can create its own checkpoints locally.
- Understood why experiment results do not need to be tracked by default in this project: experiments can be modified and repeated according to the individual's learning process, and their generated  results can be reproduced.
- Understood why datasets should not automatically be ignored: if a dataset is required to reproduce an experiment, another person needs access to the same dataset.
- Understood that datasets we create ourselves can be tracked when they are important for reproducibility.
- Understood that dataset handling depends on whether the dataset is reproducible, redistributable, or too large/restricted to store in Git.
- Understood that `.gitignore` is used to distinguish project files that should be version-controlled from local/generated files that do not need to be tracked.
- Understood that `origin` is the name assigned to the GitHub remote connection.
- Understood that `main` is the branch used as the primary branch for our project.
- Understood that `git push -u origin main` pushes the local `main` branch to the GitHub repository represented by `origin` and establishes `origin/main` as the upstream branch.
- Understood that `-u` sets the upstream relationship so that future pushes from the local `main` branch can usually be done simply with `git push`.


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
  - Created `.gitignore` in the project root.
- Added rules to ignore:
  - `__pycache__/`
  - `*.pyc`
  - `.ipynb_checkpoints/`
  - `results/`
- Committed `.gitignore` to the local repository.
- Created a private GitHub repository for the Machine Learning Research Lab.
- Connected the local repository to the GitHub repository using `origin`.
- Renamed the local branch from `master` to `main`.
- Verified that the current branch is `main`.
- Pushed the local project to GitHub using `git push -u origin main`.
- Configured the local `main` branch to track `origin/main`.

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

- **Why should `__pycache__/` be ignored?**  
  It is automatically generated by Python and can be recreated on each machine, so it is not part of the source code.

- **Why should `.ipynb_checkpoints/` be ignored?**  
  Jupyter creates these checkpoints locally, so they do not need to be version-controlled.

- **Should experiment results be tracked?**  
  Not by default for this project. Our experiments are intended to be modified and repeated for learning, so generated results can be regenerated. Important final artifacts can be tracked separately later if needed.

- **Should datasets be ignored?**  
  Not automatically. If a dataset is needed to reproduce an experiment, it should be available to others when possible. Datasets we create ourselves can be tracked. Large or restricted external datasets may instead require download instructions.

- **What does `origin` mean?**  
  `origin` is the name assigned to the remote GitHub repository connected to our local repository.

- **Why rename `master` to `main`?**  
  `main` is the commonly used modern/default primary branch name.

- **What does `git push -u origin main` mean?**  
  It pushes the local `main` branch to the `main` branch of the GitHub repository represented by `origin` and sets that remote branch as the upstream for local `main`.

- **What does `-u` do?**  
  It establishes the upstream tracking relationship between local `main` and `origin/main`, allowing future pushes to usually be performed with just `git push`.

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

- I can create a `.gitignore` file and explain why generated/local files should be ignored.
- I can identify why `__pycache__/` and `.ipynb_checkpoints/` should not be committed.
- I can reason about whether datasets and experiment results should be tracked based on reproducibility and project requirements.
- I can connect a local Git repository to GitHub using a remote.
- I can verify the configured remote using `git remote -v`.
- I can rename a branch using `git branch -M main`.
- I can verify the current branch using `git branch`.
- I can push the project to GitHub using `git push -u origin main`.
- I understand why future pushes can usually use `git push` after upstream tracking has been configured.

### Next task

Begin the complete Logistic Regression module:
- Understand the mathematical reasoning and equations.
- Design the algorithm implementation from scratch.
- Decide the required classes/functions, parameters, and return values.
- Implement the training and prediction process.
- Add appropriate metrics.
- Create visualizations to understand model behavior.
- Run experiments to study how parameters affect the algorithm.