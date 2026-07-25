package com.rs.backend.service;

import com.rs.backend.dto.PredictionRequest;
import com.rs.backend.dto.PredictionResponse;
import org.springframework.stereotype.Service;

@Service
public class PredictionService {

    public PredictionResponse predict(PredictionRequest request) {

        return new PredictionResponse(5, "XGBoost", "SUCCESS");
    }

}