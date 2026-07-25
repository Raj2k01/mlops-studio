package com.rs.backend.service;

import com.rs.backend.dto.PredictionRequest;
import com.rs.backend.dto.PredictionResponse;
import org.springframework.stereotype.Service;

@Service
public class PredictionService {

    private final PredictionClient predictionClient;

    public PredictionService(PredictionClient predictionClient) {
        this.predictionClient = predictionClient;
    }

    public PredictionResponse predict(PredictionRequest request) {

        int prediction = predictionClient.predict(request);
        return new PredictionResponse(prediction, "XGBoost", "SUCCESS");
    }
}