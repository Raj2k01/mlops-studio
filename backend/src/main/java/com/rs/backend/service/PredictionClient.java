package com.rs.backend.service;
import com.rs.backend.dto.PredictionRequest;

public interface PredictionClient {
    int predict(PredictionRequest request);
}