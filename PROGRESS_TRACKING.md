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



**## Date**

- 14-09-2026

**### Time spent**

- approx 9 hrs

**### Concepts learned**

- Binary classification using Logistic Regression

- Why Logistic Regression predicts probabilities instead of directly predicting classes.

- Linear score: `z = theta.T @ x`

- Sigmoid function and its interpretation as the probability of class 1.

- Bernoulli probability model for binary classification.

- Likelihood and maximum likelihood estimation.

- Why logarithm is applied to the likelihood.

- Negative log-likelihood as the Logistic Regression loss function.

- Derivation of the Logistic Regression gradient.

- Gradient descent and why the gradient is subtracted during minimization.

- Matrix form of the Logistic Regression gradient.

- Matrix dimensions and shape checking during implementation.

- Intercept handling using a column of ones.

- Difference between Logistic Regression gradient and the Linear Regression normal equation.

- Numerical stability of the sigmoid function.

- Numerical stability when calculating logarithms of probabilities.

- Convergence using the parameter update magnitude.

- Difference between convergence and model accuracy.

- Purpose of `max_iter` and `eps`.

- Parameter history, loss history, and log-likelihood history.

- Effect of learning rate on optimization.

- Effect of convergence tolerance on optimization.

- Behavior of Logistic Regression on linearly separable and non-separable data.

- Decision boundary and its relationship with the sigmoid threshold of 0.5.

- Matplotlib visualization of sigmoid curves, decision boundaries, loss, parameters, and update magnitude.

- NumPy concepts including `np.diff()`, axes, tuple axes, `np.linalg.norm()`, array shapes, and multidimensional slicing.

- Introduction to L2 regularization and why it is useful for controlling large parameter values.

- Role of lambda as the regularization strength.

**### Mathematical reasoning understood**

- The complete Logistic Regression reasoning:

  `X, theta -> z -> h -> J -> gradient -> theta_new -> ||delta_theta|| -> convergence`

- Understood that `z = theta.T @ x` can take any real value, so the sigmoid is used to convert it into a probability between 0 and 1.

- Understood:

  `h_theta(x) = P(y = 1 | x; theta)`

- Understood the unified Bernoulli probability:

  `P(y | x; theta) = h^y * (1 - h)^(1-y)`

- Understood that maximizing likelihood is equivalent to maximizing log-likelihood because the logarithm is monotonic.

- Understood that minimizing negative log-likelihood gives the Logistic Regression cost function.

- Derived the gradient:

  `gradient = (1/m) * X.T @ (h - y)`

- Understood the dimensions:

  `X: m x n`

  `theta: n x 1`

  `X.T: n x m`

  `h - y: m x 1`

  resulting in a gradient of shape:

  `n x 1`

- Understood that the gradient points toward increasing cost, so gradient descent moves in the opposite direction:

  `theta_new = theta_current - alpha * gradient`

- Understood that convergence is based on the change in the parameter vector:

  `||theta_new - theta_current|| < eps`

- Understood that convergence only means the optimization has stopped making significant parameter changes; it does not mean that the classifier has perfect accuracy.

- Understood the relationship:

  `theta_new - theta_current = -alpha * gradient`

  and therefore:

  `||delta_theta|| = alpha * ||gradient||`

- Understood that for binary classification:

  `h = 0.5 <=> z = 0`

  so the decision boundary is obtained from:

  `theta.T @ x = 0`

- For one feature with an intercept:

  `theta_0 + theta_1 * x = 0`

  giving:

  `x = -theta_0 / theta_1`

- Understood that the horizontal 0.5 line in the sigmoid plot is the probability threshold, while the vertical line represents the corresponding feature-space decision boundary.

- Understood that linearly separable data can cause the parameter magnitude to continue increasing while the loss continues decreasing, meaning a finite optimum may not exist.

- Understood that non-separable data can have a finite optimum and allow the optimization to converge.

- Understood the motivation for L2 regularization:

  `J_reg = J + lambda * sum(theta_j^2)`

  where the intercept `theta_0` is not included in the regularization penalty.

- Understood that the regularization gradient for an individual parameter is:

  `d(reg)/d(theta_j) = 2 * lambda * theta_j`

- Understood that the regularization gradient pushes positive parameters toward zero and negative parameters upward toward zero.

- Understood that lambda controls the strength of the regularization penalty.

- Understood that regularization creates a trade-off between fitting the data and keeping parameter values small.

**### Implementation**

- Created the Logistic Regression implementation in:

  `algorithms/supervised/logistic_regression.py`

- Designed the `LogisticRegression` class and its parameters.

- Implemented initialization of theta.

- Implemented the sigmoid function.

- Implemented the Logistic Regression loss.

- Implemented the gradient calculation.

- Implemented log-likelihood calculation.

- Implemented the training loop using gradient descent.

- Implemented convergence checking using the parameter update magnitude.

- Implemented parameter history.

- Implemented loss history.

- Implemented log-likelihood history.

- Implemented probability prediction using `predict_proba()`.

- Implemented class prediction using `predict()`.

- Added numerical stability for sigmoid calculations.

- Added clipping when calculating logarithms of probabilities.

- Created Logistic Regression tests in:

  `tests/test_logistic_regression.py`

* Learned to run the test module using:

  `python -m tests.test_logistic_regression`

* Created the learning-rate experiment in:

  `experiments/learning_rate_logistic_regression.py`

* Compared learning rates:

  - `0.01`
  - `1.0`
  - `10.0`

* Created the convergence-tolerance experiment in:

  `experiments/convergence_tolerance_logistic_regression.py`

* Compared convergence tolerances:

  - `1e-2`
  - `1e-5`
  - `1e-8`

* Created visualizations for:

  - Sigmoid probability curve
  - Decision boundary
  - Loss vs iteration
  - Parameter values vs iteration
  - Parameter update magnitude vs iteration

**### Questions + resolutions**

* **Why does Logistic Regression use a sigmoid?**

  - Because `X @ theta` can take any real value, while a probability must lie between 0 and 1.

* **Why do we use negative log-likelihood as the loss?**

  - Maximizing likelihood is equivalent to minimizing negative log-likelihood.

* **Why is the gradient subtracted?**

  - The gradient points toward increasing cost, so subtracting it moves toward lower cost.

* **Why is `X.T` an `n x m` matrix?**

  - Because `X` has shape `m x n`, so transposing swaps its dimensions.

* **Why doesn't Logistic Regression use the Linear Regression normal equation?**

  - Logistic Regression contains the nonlinear sigmoid function, so there is no equivalent simple closed-form solution.

* **Why can the parameters become extremely large with linearly separable data?**

  - Increasing the magnitude of the parameters can make the predictions increasingly confident while continuing to reduce the loss, so a finite optimum may not exist.

* **Does convergence mean the model has high accuracy?**

  - No. Convergence describes the optimization process, while accuracy describes prediction performance.

* **Why do we store theta history?**

  - To observe how the parameters change during optimization and visualize convergence.

* **Why does `theta_history` have shape `(165, 2, 1)` instead of `(165, 2)`?**

  - Each stored parameter vector has shape `(2, 1)`, so adding the iteration dimension produces `(165, 2, 1)`.

* **Why is `axis=0` used with `np.diff()`?**

  - Axis 0 represents consecutive iterations, so taking the difference along it gives the parameter update between iterations.

* **Why are tuple axes used with `np.linalg.norm()`?**

  - The parameter dimensions need to be reduced while keeping one scalar update magnitude for each iteration.

* **Why are there 164 updates when there are 165 parameter snapshots?**

  - The first snapshot is the initial parameter value, so 165 snapshots produce 164 consecutive changes.

* **What happens when the learning rate is too small?**

  - Updates become very small and convergence becomes slow.

* **What happens when the learning rate is too large?**

  - Updates can overshoot the low-loss region and cause unstable optimization or failure to converge.

* **What happens when epsilon is very large?**

  - Training can stop too early before reaching a sufficiently good solution.

* **What happens when epsilon is extremely small?**

  - More iterations are required, but the improvement may become negligible.

* **Why do multiple curves sometimes overlap in the plots?**

  - The models can produce very similar behavior, or one curve can be visually compressed by another model with a much larger scale.

* **Why introduce regularization?**

  - To penalize large parameter values and help control the parameter growth observed with linearly separable data.

* **Why don't we regularize `theta_0`?**

  - The intercept controls the location of the decision boundary and is normally excluded from the L2 penalty.

* **What does lambda represent?**

  - Lambda controls how strongly large parameter values are penalized.

* **Why does L2 regularization push parameters toward zero?**

  - Its gradient is proportional to the parameter itself:

    `2 * lambda * theta_j`

    so positive parameters are pushed downward and negative parameters are pushed upward toward zero.

**### What I can rebuild from memory**

- I can rebuild the Logistic Regression class structure without looking at the implementation.

- I can explain the purpose of each major function in the class.

- I can rebuild the training loop conceptually.

- I can explain the sigmoid, loss, gradient, parameter update, and convergence process.

- I can reason about the required matrix dimensions and shapes.

- I can rebuild the prediction process.

- I can design learning-rate and convergence-tolerance experiments.

- I can create the required visualizations and explain what each visualization represents.

- I can use NumPy operations such as `np.diff()` and `np.linalg.norm()` for analyzing parameter updates.

- I can reason about separable and non-separable datasets.

- I can explain the motivation for L2 regularization and derive its gradient.

- I still need my mathematical notes when I want to reproduce the exact derivations and equations from the theory.

**### Next task**

- Continue Logistic Regression with **L2 regularization**.

- Design an experiment to compare Logistic Regression with different values of lambda.

- Investigate how regularization affects parameter magnitude, loss, convergence, and decision boundary.

- Use the previously studied separable dataset to investigate whether regularization prevents the parameter values from growing without bound.

- After understanding regularization behavior, investigate classification performance using accuracy and other appropriate metrics.

# Progress Tracking

## 15/09/2026

### Time spent
Approximately 3 hours.

### Concepts learned
- Started Logistic Regression regularization experiments.
- Understood why regularization is added to the Logistic Regression objective.
- Understood the difference between:
  - data loss
  - regularization penalty
  - total regularized loss
- Understood that `lambda_reg` is a hyperparameter controlling regularization strength.
- Understood that increasing lambda does not directly make theta larger; instead, it increases the penalty on large parameter values.
- Understood that regularization does not impose a hard upper bound on theta.
- Learned that an excessively large learning rate can make gradient descent unstable even when regularization is present.
- Understood the interaction between learning rate and regularization strength.
- Confirmed that the intercept parameter theta_0 is excluded from L2 regularization.

### Mathematical reasoning understood
Regularized Logistic Regression objective:

J_reg(theta) = J_data(theta) + lambda_reg * sum(theta_j^2)

where the intercept theta_0 is excluded from the regularization term.

Regularization gradient for non-intercept parameters:

d/d(theta_j) [lambda_reg * theta_j^2]
= 2 * lambda_reg * theta_j

Therefore:

gradient_total
= gradient_data + gradient_regularization

and the update becomes:

theta_new
= theta_current - alpha * gradient_total

Also examined the simplified regularization-only update:

theta_new = (1 - 2 * alpha * lambda_reg) theta

This showed why a large learning rate can cause instability.

### Implementation
- Modified the existing `LogisticRegression` class to accept:
  `lambda_reg`
- Added regularization to `compute_loss()`.
- Added the regularization gradient to `compute_gradient()`.
- Excluded theta_0 from regularization.
- Kept `lambda_reg=0` as the default so the original Logistic Regression behavior remains unchanged.
- Tested the modified implementation against the previous unregularized result.

### Questions + resolutions
- Why can theta become very large even when regularization is present?
  - Regularization changes the objective and adds a force toward zero, but it does not impose a hard limit on theta.
  - A learning rate that is too large can cause gradient descent to overshoot and become unstable.
- Why did lambda=1 become unstable with learning rate=1?
  - The regularization component alone gives an update factor of:
    `(1 - 2 * alpha * lambda)`
  - With alpha=1 and lambda=1, this factor becomes -1, causing the parameter to flip rather than shrink.
- Why did reducing the learning rate to 0.1 fix the instability?
  - The smaller step size made the optimization stable.

### What I can rebuild from memory
- Explain why L2 regularization is added to the Logistic Regression objective.
- Derive the regularization gradient.
- Explain why theta_0 is excluded.
- Explain the difference between lambda and learning rate.
- Explain why a large learning rate can cause divergence despite regularization.
- Implement the regularization term and gradient in the Logistic Regression class.

### Next task
Study how to use a validation set to select the regularization hyperparameter lambda.


## 16/09/2026

### Time spent
Approximately 3 hours.

### Concepts learned
- Understood why a validation set is needed when selecting hyperparameters.
- Distinguished between parameters and hyperparameters:
  - theta = learned parameter
  - lambda = hyperparameter chosen by us
- Understood the roles of:
  - training set → learn theta
  - validation set → evaluate/select hyperparameters
  - test set → final evaluation after model choices are made
- Understood that validation data should not be used to update theta.
- Understood the relationship between overfitting, training loss, and validation loss.
- Understood that a validation loss higher than training loss by itself does not prove overfitting.
- Understood that validation loss can occasionally be lower than training loss because the particular validation examples may be easier.

### Mathematical reasoning understood
For a chosen lambda:

Training data:
X_train, y_train
→ learn theta

Validation data:
X_validation, y_validation
→ evaluate the learned theta

The validation loss used for comparison is the data loss without adding the training regularization penalty.

Therefore validation evaluation uses:

compute_loss(..., include_regularization=False)

The goal is to compare:

J_validation(lambda)

for different lambda values.

### Implementation
- Created:
  `experiments/validation_logistic_regression.py`
- Generated a synthetic binary classification dataset using two Gaussian classes.
- Used:
  - 100 examples for class 0
  - 100 examples for class 1
  - class 0 mean = [0, 0]
  - class 1 mean = [2, 2]
  - covariance = [[1, 0], [0, 1]]
- Created labels for both classes.
- Performed a stratified 80/20 train-validation split:
  - 80 class-0 training examples
  - 80 class-1 training examples
  - 20 class-0 validation examples
  - 20 class-1 validation examples
- Added the intercept as the first column of X.
- Trained Logistic Regression models for:
  lambda = [0, 0.01, 0.1, 1]
- Calculated training and validation losses.
- Visualized the learned decision boundaries.
- Plotted training and validation loss against lambda.
- Calculated validation-training loss gaps.

### Questions + resolutions
- Does validation loss being higher than training loss automatically mean overfitting?
  - No. The difference alone is not sufficient to conclude overfitting.
  - Overfitting is about poor generalization relative to training performance and should be considered more broadly.
- If we check only validation loss, how do we select lambda?
  - For a particular validation split, the lambda with the lowest validation loss is the selected candidate.

### What I can rebuild from memory
- Explain why validation data is separate from training data.
- Explain why validation loss is calculated without the regularization penalty.
- Explain how validation loss can be used to select lambda.
- Explain why one random train-validation split may not give a stable estimate.

### Next task
Understand why one validation split may be unreliable and learn K-fold cross-validation.


## 17/09/2026

### Time spent
Approximately 3 hours.

### Concepts learned
- Refactored the validation Logistic Regression experiment.
- Reinforced the importance of placing the intercept column correctly.
- Confirmed that the model expects:
  X = [1, x_1, x_2]
- Understood the effect of repeatedly running an experiment containing random data generation and random train/validation splitting.
- Observed that the exact validation-training loss gap changes between runs.
- Understood that different random splits can produce different measured validation performance.
- This motivated the need for cross-validation.

### Mathematical reasoning understood
For Logistic Regression with an intercept:

z = theta_0 + theta_1 x_1 + theta_2 x_2

Decision boundary:

theta_0 + theta_1 x_1 + theta_2 x_2 = 0

Therefore:

x_2 = -(theta_0 + theta_1 x_1) / theta_2

The decision boundary depends on the learned theta values, which can change when lambda changes.

### Implementation
- Refactored:
  `experiments/validation_logistic_regression.py`
- Removed obsolete commented-out training code.
- Removed the earlier model-training block that occurred before adding the intercept.
- Added the intercept before training the models.
- Renamed:
  - `loss_model` → `validation_losses`
  - `x_1` → `x_1_values`
  - `x_2` → `decision_boundaries`
- Kept separate training and validation loss calculations.
- Compared validation loss and training loss through:
  validation loss - training loss
- Re-ran the experiment multiple times.

### Observations
Different runs produced different validation-training gaps because the dataset and train/validation split are randomized.

Examples of observed gaps included:

Run 1:
[0.0308884, -0.0112879, -0.0840357, -0.0693505]

Run 2:
[0.0195188, -0.0337708, -0.1045794, -0.0799601]

Run 3:
[-0.0474412, -0.0819891, -0.1256863, -0.0893753]

The exact values changed, but this was expected because each execution generates new data and a new split.

### Questions + resolutions
- Why can validation loss be lower than training loss?
  - The validation set can contain examples that are easier for the learned model than the particular training examples.
  - Therefore validation loss does not have to be higher than training loss.
- Why did the gap change between runs?
  - The Gaussian data generation is random.
  - The per-class indices are also randomly shuffled.
  - Therefore both the dataset and train/validation membership change.

### What I can rebuild from memory
- Explain why the intercept must be the first column for the current Logistic Regression implementation.
- Explain how the decision boundary equation is obtained.
- Explain why random train/validation splits can produce different results.
- Explain why one validation split is not necessarily a reliable basis for choosing lambda.

### Next task
Understand K-fold cross-validation before implementing it.


## 18/09/2026

### Time spent
Approximately 3 hours.

### Concepts learned
- Started learning K-fold cross-validation conceptually.
- Understood the motivation for using multiple validation subsets instead of relying on one random validation split.
- Understood that with 5-fold cross-validation, 200 examples are divided into 5 folds of approximately 40 examples each.
- Understood that each fold is used as the validation set once.
- Understood that the remaining four folds are used as training data during that round.
- Understood that every example is therefore used for validation once and for training in the other rounds.
- Understood that cross-validation provides a more reliable estimate of expected performance on unseen data than one random train-validation split.
- Understood that cross-validation does not prove generalization capability; it provides a more stable estimate of it.

### Mathematical reasoning understood
For K-fold cross-validation:

K = 5

Number of examples per fold:

200 / 5 = 40

For each fold:

training data = all folds except the current validation fold

validation data = current fold

The process is repeated for every fold.

For each lambda, the validation losses from all folds are averaged:

CV(lambda)
= (1/K) * sum_{k=1}^{K} J_validation^(k)(lambda)

The lambda with the lowest average cross-validation validation loss is selected by the procedure.

### Implementation / experiment design
- Planned a new experiment:
  `experiments/cross_validation_logistic_regression.py`
- Established that a new Logistic Regression model must be trained for every fold because the training data changes between folds.
- For 5 folds and 4 lambda values:

  5 × 4 = 20 separate model-training processes

- Each of these models learns its own theta.
- The models are not simply reused between folds because each fold has a different training dataset.

### Questions + resolutions
- Why average validation loss across folds?
  - To obtain a more reliable estimate of model performance across different validation subsets rather than depending on one particular split.
- Do we reuse the same trained model for different folds?
  - No. Since the training data changes, a new model must be trained and a new theta must be learned for each fold.

### What I can rebuild from memory
- Explain the basic idea of K-fold cross-validation.
- Explain why every example gets used for validation once.
- Explain why a new model must be trained for every fold.
- Calculate the number of models trained for K folds and multiple lambda values.
- Explain how average cross-validation validation loss is calculated.
- Explain how cross-validation can be used for lambda selection.

### Next task
Design and implement the K-fold cross-validation experiment from scratch without using scikit-learn.