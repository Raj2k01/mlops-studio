package com.rs.backend.contoller;

import com.rs.backend.dto.PredictionRequest;
import com.rs.backend.dto.PredictionResponse;
import com.rs.backend.service.PredictionService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1")
public class PredictionController {

    private final PredictionService predictionService;

    public PredictionController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }

    @PostMapping("/predict")
    public PredictionResponse predict(@RequestBody PredictionRequest request) {
        return predictionService.predict(request);
    }
}