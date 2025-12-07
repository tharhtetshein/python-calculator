# Python Calculator

A simple calculator application demonstrating GitHub Actions CI/CD best practices.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Power/exponentiation function
- Comprehensive test coverage
- CI/CD pipeline with GitHub Actions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import add, subtract, multiply, divide, power

# Basic operations
result = add(5, 3)        # 8
result = subtract(10, 4)   # 6
result = multiply(3, 7)    # 21
result = divide(15, 3)     # 5.0
result = power(2, 8)       # 256
```

## Development

### Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest -v --cov=calculator --cov-report=term-missing

# Run specific test categories
pytest -v -m basic    # Basic operation tests
pytest -v -m edge     # Edge case tests
pytest -v -m slow     # Performance tests
```

### Linting

```bash
flake8 calculator.py test_calculator.py --max-line-length=100
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment.

### Workflow Jobs

1. **Lint** - Code quality checks using flake8
2. **Test Scenarios** - Parallel testing of different test categories
3. **Test** - Matrix testing across multiple OS and Python versions
4. **Deploy** - Conditional deployment to production (main branch only)

### Workflow Features

- ✅ Dependency caching for faster builds
- ✅ Pinned action versions for security and stability
- ✅ Matrix testing across OS (Ubuntu, Windows, macOS) and Python versions (3.9, 3.11, 3.12, 3.13-dev)
- ✅ Parallel test execution for different scenarios
- ✅ Coverage reporting with artifacts
- ✅ Conditional deployment (main branch only)
- ✅ Debug mode support
- ✅ Fail-fast disabled for comprehensive testing

### Required Secrets

This project currently uses no secrets. If you need to add secrets for deployment:

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add your secrets (e.g., `DEPLOY_TOKEN`, `API_KEY`)

**Security Best Practice:** Never commit secrets to your repository!

### Enabling Debug Logging

To see detailed debug information in workflow runs:

1. Go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `ACTIONS_STEP_DEBUG`
4. Value: `true`
5. Save the secret

Debug steps will now show additional information in workflow runs.

### Environment Protection

The deployment job uses the `production` environment. To add protection rules:

1. Go to Settings → Environments
2. Click on "production" (or create it)
3. Add protection rules:
   - Required reviewers
   - Wait timer
   - Deployment branches (restrict to main)

## Test Markers

Tests are organized using pytest markers:

- `@pytest.mark.basic` - Basic arithmetic operations
- `@pytest.mark.edge` - Edge cases (division by zero, negative exponents)
- `@pytest.mark.slow` - Performance tests with large numbers

## Project Structure

```
python-calculator/
├── calculator.py           # Main calculator module
├── test_calculator.py      # Test suite
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── config.py              # Configuration file
├── .github/
│   └── workflows/
│       └── test.yml       # CI/CD workflow
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is for educational purposes.
