# EDIAQI Task 4.5 Repository

This repository is dedicated to EDIAQI Task 4.5.

In this repository, data is sent by the user, preprocessed, and then a simple linear regression model is applied for predictions. Two models are used for each of the seven pollutants: Total Volatile Organic Compounds (TVOC), PM10, PM2.5, CO2, temperature, relative humidity (RH), and pressure. One model operates when the filtration unit is active, and the other operates when it is not. The processed data is then sent back to the user and displayed on the user interface (UI).

The linear regression model used is a hybrid of a machine learning model and a physical model. The physical models applied include gas tracking for gaseous phases and mass balance for solid particles.

## Testing Procedures

For testing purposes, two approaches are possible. The true structure of the data to be passed is defined in `settings.py` and referred to as `DUMMY_DATA`.

### Docker Testing

Build and start the Docker containers:
```
docker-compose up --build
```

### Without Docker
1. Install the virtual environment:

    ```pip install -r requirements.txt```

2. Run the FastAPI application:

    ```uvicorn main:app --reload```

3. Run the test script:

    ```python test.py```
