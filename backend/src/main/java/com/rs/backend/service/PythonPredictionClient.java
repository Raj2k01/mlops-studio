package com.rs.backend.service;
import com.rs.backend.dto.PredictionRequest;
import org.springframework.stereotype.Service;

@Service
public class PythonPredictionClient implements PredictionClient {

    @Override
    public int predict(PredictionRequest request) {
        return 5;
    }

}