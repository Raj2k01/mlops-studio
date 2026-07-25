package com.rs.backend.dto;

public record PredictionRequest(

        double fixedAcidity,
        double volatileAcidity,
        double citricAcid,
        double residualSugar,
        double chlorides,
        double freeSulfurDioxide,
        double totalSulfurDioxide,
        double density,
        double pH,
        double sulphates,
        double alcohol

) {
}