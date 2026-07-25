package com.rs.backend.service;

import com.rs.backend.dto.HealthResponse;
import org.springframework.stereotype.Service;

@Service
public class HealthService {

    public HealthResponse getHealth() {

        return new HealthResponse("UP", "MLOps Studio Backend is running");
    }
}