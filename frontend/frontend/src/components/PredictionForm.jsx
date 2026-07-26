import { useState } from "react";
import { predictWine } from "../api/predictionApi";
import {Box,Button,Grid,Paper,TextField,Typography,} from "@mui/material";
import { blue } from "@mui/material/colors";
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
    <Paper elevation={8} sx={{p: 4, color: "white",borderRadius: 3}}>
    <Typography variant="h5" gutterBottom sx={{ color: "red",fontWeight: "bold",}}>
        Wine Quality Prediction
    </Typography>

    <Typography ariant="body2" sx={{color:"black", mb: 2.3 }}>
         Enter all wine properties below.
    </Typography>

      <Box component="form" onSubmit={handleSubmit}>
        <Grid container spacing={2}>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Fixed Acidity"
              name="fixed_acidity"
              type="number"
              value={formData.fixed_acidity}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Volatile Acidity"
              name="volatile_acidity"
              type="number"
              value={formData.volatile_acidity}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Citric Acid"
              name="citric_acid"
              type="number"
              value={formData.citric_acid}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Residual Sugar"
              name="residual_sugar"
              type="number"
              value={formData.residual_sugar}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Chlorides"
              name="chlorides"
              type="number"
              value={formData.chlorides}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Free Sulfur Dioxide"
              name="free_sulfur_dioxide"
              type="number"
              value={formData.free_sulfur_dioxide}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Total Sulfur Dioxide"
              name="total_sulfur_dioxide"
              type="number"
              value={formData.total_sulfur_dioxide}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Density"
              name="density"
              type="number"
              value={formData.density}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="pH"
              name="pH"
              type="number"
              value={formData.pH}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <TextField
              fullWidth
              label="Sulphates"
              name="sulphates"
              type="number"
              value={formData.sulphates}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 6, color:"black" }}>
            <TextField
              fullWidth
              label="Alcohol"
              name="alcohol"
              type="number"
              value={formData.alcohol}
              onChange={handleChange}
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <Button type="submit" variant="contained" size="large" fullWidth sx={{mt: 2, backgroundColor: "red","&:hover": {backgroundColor: "#b71c1c"}}}>
                Predict Wine Quality
            </Button>
          </Grid>

        </Grid>

        <PredictionResult result={result}/>

      </Box>
    </Paper>
  );
}