import { useState } from "react";
import { predictWine } from "../api/predictionApi";
import {
  Box,
  Button,
  Grid,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import PredictionResult from "./PredictionResult";

export default function PredictionForm() {
  const [formData, setFormData] = useState({
    fixed_acidity: "",
    volatile_acidity: "",
    citric_acid: "",
    residual_sugar: "",
    chlorides: "",
    free_sulfur_dioxide: "",
    total_sulfur_dioxide: "",
    density: "",
    pH: "",
    sulphates: "",
    alcohol: "",
  });

  const [result, setResult] = useState(null);

  const fieldConfig = {
    fixed_acidity: {
      label: "Fixed Acidity",
      min: 4.6,
      max: 15.9,
      step: 0.1,
    },
    volatile_acidity: {
      label: "Volatile Acidity",
      min: 0.12,
      max: 1.58,
      step: 0.01,
    },
    citric_acid: {
      label: "Citric Acid",
      min: 0.0,
      max: 1.0,
      step: 0.01,
    },
    residual_sugar: {
      label: "Residual Sugar",
      min: 0.9,
      max: 15.5,
      step: 0.1,
    },
    chlorides: {
      label: "Chlorides",
      min: 0.012,
      max: 0.611,
      step: 0.001,
    },
    free_sulfur_dioxide: {
      label: "Free Sulfur Dioxide",
      min: 1,
      max: 72,
      step: 1,
    },
    total_sulfur_dioxide: {
      label: "Total Sulfur Dioxide",
      min: 6,
      max: 289,
      step: 1,
    },
    density: {
      label: "Density",
      min: 0.99007,
      max: 1.00369,
      step: 0.00001,
    },
    pH: {
      label: "pH",
      min: 2.74,
      max: 4.01,
      step: 0.01,
    },
    sulphates: {
      label: "Sulphates",
      min: 0.33,
      max: 2.0,
      step: 0.01,
    },
    alcohol: {
      label: "Alcohol",
      min: 8.4,
      max: 14.9,
      step: 0.1,
    },
  };

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const payload = {
        fixedAcidity: Number(formData.fixed_acidity),
        volatileAcidity: Number(formData.volatile_acidity),
        citricAcid: Number(formData.citric_acid),
        residualSugar: Number(formData.residual_sugar),
        chlorides: Number(formData.chlorides),
        freeSulfurDioxide: Number(formData.free_sulfur_dioxide),
        totalSulfurDioxide: Number(formData.total_sulfur_dioxide),
        density: Number(formData.density),
        pH: Number(formData.pH),
        sulphates: Number(formData.sulphates),
        alcohol: Number(formData.alcohol),
      };

      const response = await predictWine(payload);

      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Paper
      elevation={8}
      sx={{
        p: 4,
        borderRadius: 3,
      }}
    >
      <Typography
        variant="h5"
        gutterBottom
        sx={{
          color: "red",
          fontWeight: "bold",
        }}
      >
        Wine Quality Prediction
      </Typography>

      <Typography
        variant="body2"
        sx={{
          color: "black",
          mb: 3,
        }}
      >
        Enter all wine properties below.
      </Typography>

      <Box component="form" onSubmit={handleSubmit}>
        <Grid container spacing={2}>
          {Object.entries(fieldConfig).map(([key, field]) => (
            <Grid key={key} size={{ xs: 12, md: 6 }}>
              <TextField
                fullWidth
                required
                label={field.label}
                name={key}
                type="number"
                value={formData[key]}
                onChange={handleChange}
                helperText={`Range: ${field.min} - ${field.max}`}
                slotProps={{
                  htmlInput: {
                    min: field.min,
                    max: field.max,
                    step: field.step,
                  },
                }}
              />
            </Grid>
          ))}

          <Grid size={{ xs: 12 }}>
            <Button
              type="submit"
              variant="contained"
              size="large"
              fullWidth
              sx={{
                mt: 2,
                backgroundColor: "red",
                "&:hover": {
                  backgroundColor: "#b71c1c",
                },
              }}
            >
              Predict Wine Quality
            </Button>
          </Grid>
        </Grid>

        <PredictionResult result={result} />
      </Box>
    </Paper>
  );
}