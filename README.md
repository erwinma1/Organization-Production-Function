# Organization Production Function

This project estimates the relationship between staff budget (labor input) and program output in a service-based nonprofit organization using a Cobb-Douglas production function.

## Objective
Estimate the output elasticity of labor to determine how much staff cost is needed to support programming, especially under budget constraints or fiscal shocks.

## Methodology
1. Clean and transform organizational data (log-linear form).
2. Run OLS regression on `log(Output)` ~ `log(Labor)`.
3. Fit the production function.
4. Calculate point elasticities.
5. Convert back to USD values for interpretation.

## Findings
- Estimated output elasticity ≈ 0.56
- Predicted output within ±6% of actual values
- Provides a decision-support tool for staffing and budget forecasting

## Files
- `production_model.py`: Full pipeline with regression, fitting, and plotting
- `write_test_refactor_v6.xlsx`: Output from the model
- `Production Model Report Github.docx`: Technical explanation of approach and implications

## Notes
- Synthetic data is used for confidentiality.
- Inspired by [this Cobb-Douglas tutorial](https://mbounthavong.com/blog/tag/Cobb-Douglas+production+function)

## Author
Erwin Ma | 2025
