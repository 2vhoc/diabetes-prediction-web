# Diabetes Prediction Application

A web-based application that predicts the likelihood of diabetes based on user-input health metrics using machine learning.
## Web Demo
- 
## Features

- Real-time diabetes prediction using a trained machine learning model
- User-friendly web interface for data input
- Instant results with prediction probability
- Secure data handling
- RESTful API backend architecture

## Tech Stack

### Backend
- Python 3.12.3
- FastAPI - High-performance web framework
- scikit-learn - Machine learning library
- pandas - Data manipulation
- Docker - Containerization

### Data Science
- NumPy - Numerical computations
- Seaborn/Matplotlib - Data visualization
- Joblib - Model serialization

## Installation

### Prerequisites
- Docker
- Python 3.12.3 or higher

### Docker Setup
1. Clone the repository:
```bash
git clone https://github.com/2vhoc/diabetes-prediction-web.git
cd diabetes-prediction-web
```

2. Build the Docker image:
```bash
sudo docker build -t prj .
```

3. Run the container:
```bash
sudo docker run --rm -v $(pwd):/app -p 8000:8000 project
```

### Local Development Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirement.txt
```

3. Start the application:
```bash
cd back_end
uvicorn main:app --reload
```

## Usage

1. Access the application at `http://localhost:8000`
2. Enter the required health metrics:
   - Glucose level
   - Blood pressure
   - BMI
   - Age
   - Other relevant factors
3. Click "Predict" to get your results

## API Documentation

Access the API documentation at `http://localhost:8000/docs` for:
- Endpoint descriptions
- Request/response schemas
- Interactive testing interface

## Project Structure
```
project_diabetes/
├── back_end/
│   └── main.py
├── model/
│   ├── scaler.joblib
│   └── model.joblib
├── front_end/
│   └──index.html
├── dataset/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Vu Van Hoc - 2vhoc7@gmail.com
Project Link: https://github.com/2vhoc/diabetes-prediction-web.git

## Acknowledgments

- Dataset source (if applicable)
- Any third-party libraries or resources used
- Inspiration for the project