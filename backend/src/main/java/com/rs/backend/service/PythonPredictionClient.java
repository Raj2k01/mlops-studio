package com.rs.backend.service;

import com.rs.backend.dto.PredictionRequest;
import org.springframework.stereotype.Service;
import tools.jackson.databind.JsonNode;
import tools.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;

@Service
public class PythonPredictionClient implements PredictionClient {

    private static final String INPUT_FILE =
            "../ml/data/prediction_input.json";

    private static final String OUTPUT_FILE =
            "../ml/data/prediction_output.json";

    private static final String PYTHON_SCRIPT =
            "../ml/scripts/predict.py";

    private final ObjectMapper mapper = new ObjectMapper();

    @Override
    public int predict(PredictionRequest request) {

        try {

            // Write request to JSON
            mapper.writeValue(new File(INPUT_FILE), request);

            // Execute Python
            ProcessBuilder pb = new ProcessBuilder(
                    "C:\\Users\\Raj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
                    PYTHON_SCRIPT
            );

            pb.redirectErrorStream(true);

            Process process = pb.start();

            String output = new String(process.getInputStream().readAllBytes());

            int exitCode = process.waitFor();

            System.out.println("Python Output:");
            System.out.println(output);

            if (exitCode != 0) {
                throw new RuntimeException(output);
            }

            // Read prediction_output.json
            JsonNode node = mapper.readTree(new File(OUTPUT_FILE));
            return node.get("prediction").asInt();

        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}