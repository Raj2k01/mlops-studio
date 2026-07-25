package com.rs.backend.dto;

public record PredictionResponse(int prediction, String model, String status) {
}