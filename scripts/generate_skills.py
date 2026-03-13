"""Generate the full OARL skill library — 105 skills across 7 domains.

Run: python scripts/generate_skills.py
Each skill gets a Python module (__init__.py) and a SKILL.md file.
"""

from __future__ import annotations

import os
from pathlib import Path
from dataclasses import dataclass

BASE = Path(__file__).resolve().parents[1] / "src" / "skills"

SKILL_TEMPLATE = '''"""Skill: {title}"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for {title}."""

    @property
    def name(self) -> str:
        return "{name}"

    @property
    def domain(self) -> str:
        return "{domain}"

    @property
    def description(self) -> str:
        return "{description}"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the {name} skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for {name}."""
        return {{"skill": "{name}", "status": "executed", "input_keys": list(data.keys())}}
'''

SKILL_MD_TEMPLATE = '''---
name: {name}
description: {description}
---

# {title}

## Description
{description}

## When to Use
{when_to_use}

## Workflow
{workflow}

## Tools Used
{tools}

## Examples
```python
from src.skills.{domain}.{name} import Skill

skill = Skill()
result = await skill.run(SkillInput(data={{"key": "value"}}))
```

## Best Practices
{best_practices}
'''


@dataclass
class SkillDef:
    name: str
    domain: str
    title: str
    description: str
    when_to_use: str
    workflow: str
    tools: str
    best_practices: str


# ──────────────────────────────────────────────────────────────────
#  SKILL DEFINITIONS — 105 skills across 7 domains
# ──────────────────────────────────────────────────────────────────

SKILLS: list[SkillDef] = [
    # ── Data Engineering (15) ─────────────────────────────────────
    SkillDef("csv_loader", "data_engineering", "CSV Loader", "Load CSV files into DataFrames", "When ingesting CSV datasets", "1. Read file path\\n2. Parse CSV\\n3. Return DataFrame", "pandas", "Specify encoding and delimiter"),
    SkillDef("json_loader", "data_engineering", "JSON Loader", "Load JSON files into DataFrames", "When ingesting JSON data", "1. Read file\\n2. Parse JSON\\n3. Normalize nested structures", "pandas, json", "Handle nested JSON with json_normalize"),
    SkillDef("parquet_loader", "data_engineering", "Parquet Loader", "Load Parquet files into DataFrames", "When working with columnar data", "1. Read parquet file\\n2. Return DataFrame", "pandas, pyarrow", "Use pyarrow engine for best performance"),
    SkillDef("excel_loader", "data_engineering", "Excel Loader", "Load Excel files into DataFrames", "When ingesting spreadsheet data", "1. Read Excel file\\n2. Select sheet\\n3. Return DataFrame", "pandas, openpyxl", "Specify sheet name and header row"),
    SkillDef("sql_loader", "data_engineering", "SQL Loader", "Load data from SQL databases", "When querying relational databases", "1. Connect to DB\\n2. Execute query\\n3. Return DataFrame", "sqlalchemy, pandas", "Use parameterized queries"),
    SkillDef("data_cleaning", "data_engineering", "Data Cleaning", "Clean and standardize raw data", "After initial data loading", "1. Remove duplicates\\n2. Fix types\\n3. Standardize formats", "pandas", "Always document cleaning steps"),
    SkillDef("missing_value_handler", "data_engineering", "Missing Value Handler", "Detect and handle missing values", "When data has NaN/null values", "1. Detect nulls\\n2. Analyze patterns\\n3. Apply strategy", "pandas, numpy", "Choose strategy based on data type and missingness pattern"),
    SkillDef("outlier_detector", "data_engineering", "Outlier Detector", "Detect outliers using statistical methods", "When numeric data may contain anomalies", "1. Compute IQR/Z-scores\\n2. Flag outliers\\n3. Report", "pandas, scipy", "Use IQR for skewed data, Z-score for normal"),
    SkillDef("type_converter", "data_engineering", "Type Converter", "Convert column data types", "When columns have incorrect dtypes", "1. Detect current types\\n2. Infer correct types\\n3. Convert", "pandas", "Handle conversion errors gracefully"),
    SkillDef("data_merger", "data_engineering", "Data Merger", "Merge multiple DataFrames", "When combining data from multiple sources", "1. Identify join keys\\n2. Choose join type\\n3. Merge", "pandas", "Validate join keys before merging"),
    SkillDef("data_splitter", "data_engineering", "Data Splitter", "Split data into train/test/validation sets", "Before model training", "1. Stratify if needed\\n2. Split data\\n3. Validate split ratios", "sklearn", "Use stratified splits for imbalanced data"),
    SkillDef("dataset_profiler", "data_engineering", "Dataset Profiler", "Generate comprehensive dataset profiles", "As first step in any analysis", "1. Compute stats\\n2. Check quality\\n3. Generate profile", "pandas", "Run profiling before any transformations"),
    SkillDef("schema_validator", "data_engineering", "Schema Validator", "Validate data against expected schema", "After loading data or before processing", "1. Define schema\\n2. Validate types\\n3. Check constraints", "pydantic, pandas", "Define schemas as code for reproducibility"),
    SkillDef("data_sampler", "data_engineering", "Data Sampler", "Create representative data samples", "When working with very large datasets", "1. Choose strategy\\n2. Sample data\\n3. Validate distribution", "pandas", "Maintain class distribution in samples"),
    SkillDef("data_deduplicator", "data_engineering", "Data Deduplicator", "Find and remove duplicate records", "When data may contain duplicates", "1. Identify key columns\\n2. Find duplicates\\n3. Remove or merge", "pandas", "Consider fuzzy matching for near-duplicates"),

    # ── Data Science (15) ─────────────────────────────────────────
    SkillDef("eda_generator", "data_science", "EDA Generator", "Generate comprehensive exploratory data analysis", "As the first analytical step", "1. Compute stats\\n2. Create visuals\\n3. Identify patterns", "pandas, matplotlib", "Focus on distributions, correlations, and outliers"),
    SkillDef("correlation_analysis", "data_science", "Correlation Analysis", "Compute and visualize correlation matrices", "When exploring feature relationships", "1. Compute correlations\\n2. Filter significant\\n3. Visualize", "pandas, seaborn", "Use Spearman for non-linear relationships"),
    SkillDef("distribution_analysis", "data_science", "Distribution Analysis", "Analyze the statistical distribution of features", "When understanding data shape", "1. Test normality\\n2. Compute moments\\n3. Visualize", "scipy, matplotlib", "Test assumptions before parametric tests"),
    SkillDef("statistical_testing", "data_science", "Statistical Testing", "Perform hypothesis tests (t-test, chi-square, etc.)", "When validating hypotheses statistically", "1. Choose test\\n2. Check assumptions\\n3. Run test\\n4. Interpret", "scipy", "Always check test assumptions first"),
    SkillDef("hypothesis_testing", "data_science", "Hypothesis Testing", "Formulate and test research hypotheses", "When answering specific research questions", "1. State H0/H1\\n2. Choose test\\n3. Compute p-value\\n4. Decide", "scipy, statsmodels", "Report effect sizes alongside p-values"),
    SkillDef("time_series_decomposition", "data_science", "Time Series Decomposition", "Decompose time series into trend, seasonality, residual", "When analyzing temporal patterns", "1. Detect frequency\\n2. Decompose\\n3. Analyze components", "statsmodels", "Choose additive vs multiplicative based on variance"),
    SkillDef("anomaly_detection", "data_science", "Anomaly Detection", "Detect anomalous observations in data", "When finding unusual patterns or fraud", "1. Choose method\\n2. Fit detector\\n3. Score observations", "sklearn", "Combine multiple methods for robustness"),
    SkillDef("clustering_analysis", "data_science", "Clustering Analysis", "Group data into natural clusters", "When discovering natural groupings", "1. Scale features\\n2. Choose k\\n3. Fit clusters\\n4. Evaluate", "sklearn", "Use silhouette score to choose k"),
    SkillDef("dimensionality_reduction", "data_science", "Dimensionality Reduction", "Reduce feature space using PCA or t-SNE", "When dealing with high-dimensional data", "1. Scale data\\n2. Choose method\\n3. Transform\\n4. Visualize", "sklearn", "Standardize features before PCA"),
    SkillDef("feature_importance", "data_science", "Feature Importance", "Rank features by predictive importance", "When selecting features for modeling", "1. Train model\\n2. Extract importances\\n3. Rank and filter", "sklearn", "Use permutation importance for unbiased results"),
    SkillDef("data_summarizer", "data_science", "Data Summarizer", "Generate natural-language data summaries", "When presenting data to stakeholders", "1. Compute key stats\\n2. Identify highlights\\n3. Write summary", "pandas", "Focus on actionable insights"),
    SkillDef("trend_analysis", "data_science", "Trend Analysis", "Detect trends in temporal or sequential data", "When monitoring changes over time", "1. Smooth data\\n2. Fit trend\\n3. Test significance", "scipy, statsmodels", "Use rolling windows for noisy data"),
    SkillDef("seasonality_detection", "data_science", "Seasonality Detection", "Detect seasonal patterns in time series", "When analyzing cyclical behavior", "1. Compute ACF\\n2. Detect period\\n3. Validate", "statsmodels", "Use autocorrelation to find period"),
    SkillDef("cohort_analysis", "data_science", "Cohort Analysis", "Analyze behavior across user cohorts", "When studying retention or lifecycle", "1. Define cohorts\\n2. Compute metrics\\n3. Compare", "pandas", "Use time-based cohorts for retention"),
    SkillDef("ab_test_analyzer", "data_science", "A/B Test Analyzer", "Analyze results of A/B experiments", "When comparing control vs treatment", "1. Validate data\\n2. Run test\\n3. Compute confidence interval", "scipy", "Check sample size for statistical power"),

    # ── Machine Learning (20) ─────────────────────────────────────
    SkillDef("linear_regression", "machine_learning", "Linear Regression", "Train linear regression models", "For continuous target prediction", "1. Prepare data\\n2. Fit model\\n3. Evaluate", "sklearn", "Check linearity assumptions"),
    SkillDef("logistic_regression", "machine_learning", "Logistic Regression", "Train logistic regression classifiers", "For binary/multi-class classification", "1. Prepare data\\n2. Scale features\\n3. Fit\\n4. Evaluate", "sklearn", "Regularize to prevent overfitting"),
    SkillDef("random_forest", "machine_learning", "Random Forest", "Train random forest ensemble models", "For robust classification or regression", "1. Prepare data\\n2. Set hyperparams\\n3. Fit\\n4. Evaluate", "sklearn", "Tune n_estimators and max_depth"),
    SkillDef("gradient_boosting", "machine_learning", "Gradient Boosting", "Train gradient boosting models", "For high-accuracy predictions", "1. Prepare data\\n2. Configure\\n3. Fit\\n4. Evaluate", "sklearn", "Use early stopping to prevent overfitting"),
    SkillDef("xgboost_trainer", "machine_learning", "XGBoost Trainer", "Train XGBoost models", "For competitive ML performance", "1. Prepare DMatrix\\n2. Set params\\n3. Train\\n4. Evaluate", "xgboost", "Use GPU training for large datasets"),
    SkillDef("lightgbm_trainer", "machine_learning", "LightGBM Trainer", "Train LightGBM models", "For fast training on large datasets", "1. Prepare data\\n2. Set params\\n3. Train\\n4. Evaluate", "lightgbm", "Use categorical feature support"),
    SkillDef("svm_trainer", "machine_learning", "SVM Trainer", "Train support vector machine models", "For high-dimensional classification", "1. Scale features\\n2. Choose kernel\\n3. Fit\\n4. Evaluate", "sklearn", "Always scale features for SVM"),
    SkillDef("knn_trainer", "machine_learning", "KNN Trainer", "Train K-nearest neighbors models", "For instance-based classification", "1. Scale features\\n2. Choose k\\n3. Fit\\n4. Evaluate", "sklearn", "Use cross-validation to choose k"),
    SkillDef("neural_network", "machine_learning", "Neural Network", "Train neural network models", "For complex non-linear patterns", "1. Design architecture\\n2. Compile\\n3. Train\\n4. Evaluate", "sklearn", "Start simple, add complexity as needed"),
    SkillDef("auto_ml", "machine_learning", "AutoML", "Automated model selection and tuning", "For rapid prototyping", "1. Define search space\\n2. Run trials\\n3. Select best", "sklearn", "Set time and resource limits"),
    SkillDef("hyperparameter_tuner", "machine_learning", "Hyperparameter Tuner", "Optimize model hyperparameters", "After initial model training", "1. Define search space\\n2. Choose strategy\\n3. Search\\n4. Validate", "sklearn", "Use random search before grid search"),
    SkillDef("cross_validator", "machine_learning", "Cross Validator", "Perform k-fold cross-validation", "When estimating model generalization", "1. Choose k\\n2. Split data\\n3. Train and evaluate each fold", "sklearn", "Use stratified folds for classification"),
    SkillDef("model_selector", "machine_learning", "Model Selector", "Compare and select the best model", "After training multiple candidates", "1. Collect results\\n2. Compare metrics\\n3. Select best", "sklearn", "Consider both accuracy and complexity"),
    SkillDef("ensemble_builder", "machine_learning", "Ensemble Builder", "Build model ensembles (voting, stacking)", "When combining model strengths", "1. Select base models\\n2. Choose strategy\\n3. Build ensemble", "sklearn", "Use diverse models for better ensembles"),
    SkillDef("pipeline_builder", "machine_learning", "Pipeline Builder", "Build sklearn preprocessing pipelines", "When standardizing ML workflows", "1. Define steps\\n2. Build pipeline\\n3. Validate", "sklearn", "Include preprocessing in the pipeline"),
    SkillDef("feature_engineer", "machine_learning", "Feature Engineer", "Create new features from existing data", "Before model training", "1. Analyze features\\n2. Create interactions\\n3. Validate", "pandas, sklearn", "Test feature impact with ablation"),
    SkillDef("target_encoder", "machine_learning", "Target Encoder", "Encode categorical targets for ML", "When targets are categorical", "1. Detect type\\n2. Choose encoding\\n3. Transform", "sklearn", "Use ordinal encoding for ordered categories"),
    SkillDef("model_serializer", "machine_learning", "Model Serializer", "Save and load trained models", "After model training for deployment", "1. Serialize model\\n2. Save to file\\n3. Verify load", "joblib", "Include preprocessing in saved artifacts"),
    SkillDef("prediction_service", "machine_learning", "Prediction Service", "Generate predictions from trained models", "When making predictions on new data", "1. Load model\\n2. Validate input\\n3. Predict\\n4. Format output", "sklearn", "Validate input schema before prediction"),
    SkillDef("model_comparator", "machine_learning", "Model Comparator", "Compare models side-by-side on metrics", "When choosing between model candidates", "1. Collect models\\n2. Evaluate each\\n3. Create comparison table", "sklearn, pandas", "Use same test set for fair comparison"),

    # ── Visualization (10) ────────────────────────────────────────
    SkillDef("bar_chart", "visualization", "Bar Chart", "Generate bar chart visualizations", "When comparing categories", "1. Prepare data\\n2. Configure chart\\n3. Render", "matplotlib, seaborn", "Sort bars by value for readability"),
    SkillDef("line_chart", "visualization", "Line Chart", "Generate line chart visualizations", "When showing trends over time", "1. Prepare data\\n2. Configure axes\\n3. Render", "matplotlib", "Use markers for discrete data points"),
    SkillDef("scatter_plot", "visualization", "Scatter Plot", "Generate scatter plot visualizations", "When exploring variable relationships", "1. Prepare data\\n2. Configure\\n3. Add regression line", "matplotlib, seaborn", "Use color for additional dimensions"),
    SkillDef("histogram", "visualization", "Histogram", "Generate histogram visualizations", "When analyzing distributions", "1. Choose bins\\n2. Configure\\n3. Render", "matplotlib", "Use Freedman-Diaconis rule for bin count"),
    SkillDef("heatmap", "visualization", "Heatmap", "Generate heatmap visualizations", "When showing correlation or frequency matrices", "1. Prepare matrix\\n2. Choose colormap\\n3. Render", "seaborn", "Annotate cells with values"),
    SkillDef("box_plot", "visualization", "Box Plot", "Generate box plot visualizations", "When comparing distributions across groups", "1. Group data\\n2. Configure\\n3. Render", "seaborn", "Show individual points for small datasets"),
    SkillDef("pie_chart", "visualization", "Pie Chart", "Generate pie chart visualizations", "When showing proportions of a whole", "1. Compute shares\\n2. Configure\\n3. Render", "matplotlib", "Limit to 6-7 slices maximum"),
    SkillDef("dashboard_generator", "visualization", "Dashboard Generator", "Generate multi-panel dashboards", "When presenting multiple metrics", "1. Select panels\\n2. Layout\\n3. Render", "plotly", "Use consistent color scheme"),
    SkillDef("interactive_plot", "visualization", "Interactive Plot", "Generate interactive Plotly visualizations", "When users need to explore data", "1. Prepare data\\n2. Build figure\\n3. Add interactivity", "plotly", "Add tooltips for context"),
    SkillDef("report_chart", "visualization", "Report Chart", "Generate publication-quality charts", "When including charts in reports", "1. Style chart\\n2. Add labels\\n3. Export high-DPI", "matplotlib", "Use consistent typography"),

    # ── Research (15) ─────────────────────────────────────────────
    SkillDef("report_writer", "research", "Report Writer", "Generate structured research reports", "After analysis is complete", "1. Outline sections\\n2. Write content\\n3. Format", "jinja2", "Follow IMRaD structure"),
    SkillDef("insight_extractor", "research", "Insight Extractor", "Extract key insights from analysis results", "After data analysis", "1. Review results\\n2. Identify patterns\\n3. Summarize", "pandas", "Prioritize actionable insights"),
    SkillDef("summary_generator", "research", "Summary Generator", "Generate executive summaries", "When creating reports for stakeholders", "1. Identify key points\\n2. Prioritize\\n3. Write summary", "jinja2", "Keep under 1 page"),
    SkillDef("citation_manager", "research", "Citation Manager", "Manage and format research citations", "When referencing external sources", "1. Collect sources\\n2. Format citations\\n3. Build bibliography", "jinja2", "Use consistent citation format"),
    SkillDef("paper_searcher", "research", "Paper Searcher", "Search for relevant academic papers", "When conducting literature review", "1. Define keywords\\n2. Search databases\\n3. Rank results", "httpx", "Use multiple search sources"),
    SkillDef("knowledge_synthesizer", "research", "Knowledge Synthesizer", "Synthesize knowledge from multiple sources", "When combining findings", "1. Collect sources\\n2. Identify themes\\n3. Synthesize", "pandas", "Use structured frameworks for synthesis"),
    SkillDef("methodology_writer", "research", "Methodology Writer", "Write methodology sections for reports", "When documenting analysis methods", "1. Describe approach\\n2. List tools\\n3. Document parameters", "jinja2", "Include reproducibility information"),
    SkillDef("results_formatter", "research", "Results Formatter", "Format analysis results for presentation", "When preparing results for reports", "1. Select key results\\n2. Format tables\\n3. Create figures", "pandas, matplotlib", "Use consistent number formatting"),
    SkillDef("abstract_writer", "research", "Abstract Writer", "Generate research abstracts", "When creating report summaries", "1. Summarize objective\\n2. Key findings\\n3. Conclusions", "jinja2", "Follow structured abstract format"),
    SkillDef("literature_reviewer", "research", "Literature Reviewer", "Conduct systematic literature reviews", "When surveying existing research", "1. Define scope\\n2. Search\\n3. Analyze\\n4. Summarize", "httpx", "Use PRISMA guidelines"),
    SkillDef("finding_validator", "research", "Finding Validator", "Validate research findings", "When verifying analysis results", "1. Cross-check data\\n2. Validate stats\\n3. Confirm conclusions", "scipy", "Use multiple validation methods"),
    SkillDef("recommendation_engine", "research", "Recommendation Engine", "Generate actionable recommendations", "When providing guidance from analysis", "1. Identify actions\\n2. Assess feasibility\\n3. Prioritize", "pandas", "Rank by impact and effort"),
    SkillDef("research_planner", "research", "Research Planner", "Plan research investigations", "At the start of new research", "1. Define questions\\n2. Plan methods\\n3. Estimate resources", "pandas", "Start with clear hypotheses"),
    SkillDef("data_storyteller", "research", "Data Storyteller", "Create compelling data narratives", "When presenting findings to audiences", "1. Build narrative arc\\n2. Select evidence\\n3. Write story", "jinja2", "Lead with the key insight"),
    SkillDef("executive_summary", "research", "Executive Summary Writer", "Write executive summaries from analysis", "When reporting to leadership", "1. Identify decisions\\n2. Summarize findings\\n3. State actions", "jinja2", "Keep under 2 pages"),

    # ── Evaluation (10) ───────────────────────────────────────────
    SkillDef("accuracy_evaluator", "evaluation", "Accuracy Evaluator", "Compute classification accuracy metrics", "After model training", "1. Generate predictions\\n2. Compute accuracy\\n3. Report", "sklearn", "Report confidence intervals"),
    SkillDef("precision_recall", "evaluation", "Precision-Recall Evaluator", "Compute precision and recall metrics", "For classification evaluation", "1. Compute precision\\n2. Compute recall\\n3. Compute F1", "sklearn", "Use macro/micro averaging for multi-class"),
    SkillDef("roc_auc", "evaluation", "ROC-AUC Evaluator", "Compute ROC curves and AUC scores", "For binary classification evaluation", "1. Compute probabilities\\n2. Plot ROC\\n3. Compute AUC", "sklearn", "Use probability calibration first"),
    SkillDef("confusion_matrix", "evaluation", "Confusion Matrix", "Generate confusion matrices", "After classification predictions", "1. Generate matrix\\n2. Normalize\\n3. Visualize", "sklearn, seaborn", "Show both raw and normalized"),
    SkillDef("regression_metrics", "evaluation", "Regression Metrics", "Compute regression evaluation metrics", "After regression model training", "1. Compute MAE\\n2. Compute RMSE\\n3. Compute R-squared", "sklearn", "Report all three metrics together"),
    SkillDef("cross_val_scorer", "evaluation", "Cross-Validation Scorer", "Score models using cross-validation", "When estimating generalization", "1. Define scoring\\n2. Run CV\\n3. Aggregate scores", "sklearn", "Report mean and standard deviation"),
    SkillDef("model_drift_detector", "evaluation", "Model Drift Detector", "Detect data or concept drift", "When monitoring model performance", "1. Compare distributions\\n2. Test drift\\n3. Alert", "scipy", "Monitor feature-level drift"),
    SkillDef("fairness_checker", "evaluation", "Fairness Checker", "Check model fairness across groups", "Before deploying models", "1. Define groups\\n2. Compute disparity\\n3. Report", "sklearn", "Check multiple fairness metrics"),
    SkillDef("performance_profiler", "evaluation", "Performance Profiler", "Profile model inference performance", "Before deployment", "1. Measure latency\\n2. Measure throughput\\n3. Profile memory", "pandas", "Test with realistic data volumes"),
    SkillDef("experiment_comparator", "evaluation", "Experiment Comparator", "Compare multiple experiments side-by-side", "When selecting best experiment", "1. Collect experiments\\n2. Align metrics\\n3. Rank", "pandas", "Use statistical tests for comparison"),

    # ── Infrastructure (10) ───────────────────────────────────────
    SkillDef("env_setup", "infrastructure", "Environment Setup", "Set up Python environments", "At project start", "1. Create venv\\n2. Install deps\\n3. Verify", "uv", "Pin dependency versions"),
    SkillDef("dependency_manager", "infrastructure", "Dependency Manager", "Manage project dependencies", "When adding or updating packages", "1. Check compatibility\\n2. Update lock\\n3. Verify", "uv", "Use lockfiles for reproducibility"),
    SkillDef("docker_builder", "infrastructure", "Docker Builder", "Build Docker images for deployment", "When containerizing the application", "1. Write Dockerfile\\n2. Build image\\n3. Test", "docker", "Use multi-stage builds"),
    SkillDef("log_aggregator", "infrastructure", "Log Aggregator", "Aggregate and search through logs", "When debugging or monitoring", "1. Collect logs\\n2. Parse\\n3. Index\\n4. Search", "structlog", "Use structured logging format"),
    SkillDef("resource_monitor", "infrastructure", "Resource Monitor", "Monitor CPU, memory, and disk usage", "When tracking system health", "1. Collect metrics\\n2. Check thresholds\\n3. Alert", "psutil", "Set up alerts for critical resources"),
    SkillDef("cache_manager", "infrastructure", "Cache Manager", "Manage caching of computed results", "When optimizing repeated computations", "1. Define cache key\\n2. Store result\\n3. Invalidate when needed", "functools", "Set TTL for cache entries"),
    SkillDef("job_scheduler", "infrastructure", "Job Scheduler", "Schedule and manage background jobs", "When running periodic tasks", "1. Define schedule\\n2. Register job\\n3. Monitor", "asyncio", "Use cron-style scheduling"),
    SkillDef("data_versioner", "infrastructure", "Data Versioner", "Version control datasets", "When tracking dataset changes", "1. Hash dataset\\n2. Store version\\n3. Log metadata", "hashlib", "Track schema changes separately"),
    SkillDef("config_validator", "infrastructure", "Config Validator", "Validate configuration files", "At application startup", "1. Load config\\n2. Validate schema\\n3. Report errors", "pydantic", "Fail fast on invalid config"),
    SkillDef("health_checker", "infrastructure", "Health Checker", "Check system and service health", "For monitoring and alerting", "1. Check services\\n2. Verify connectivity\\n3. Report status", "httpx", "Include dependency health checks"),
]


def generate_skill(skill: SkillDef) -> None:
    """Write the Python module and SKILL.md for a single skill."""
    skill_dir = BASE / skill.domain / skill.name
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Python module
    py_content = SKILL_TEMPLATE.format(
        title=skill.title,
        name=skill.name,
        domain=skill.domain,
        description=skill.description,
    )
    (skill_dir / "__init__.py").write_text(py_content, encoding="utf-8")

    # SKILL.md documentation
    md_content = SKILL_MD_TEMPLATE.format(
        name=skill.name,
        title=skill.title,
        description=skill.description,
        when_to_use=skill.when_to_use,
        workflow=skill.workflow,
        tools=skill.tools,
        best_practices=skill.best_practices,
        domain=skill.domain,
    )
    (skill_dir / "SKILL.md").write_text(md_content, encoding="utf-8")


def main() -> None:
    for skill in SKILLS:
        generate_skill(skill)
    print(f"Generated {len(SKILLS)} skills across {len({s.domain for s in SKILLS})} domains.")


if __name__ == "__main__":
    main()
