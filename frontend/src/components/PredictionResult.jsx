import { Paper, Typography } from "@mui/material";

export default function PredictionResult({ result }) {
  if (!result) return null;

  return (
    <Paper
      elevation={4}
      sx={{
        mt: 4,
        p: 3,
        borderRadius: 2,
        backgroundColor: "#1f1f1f",
        color: "white",
      }}
    >
      <Typography
        variant="h6"
        sx={{
          color: "red",
          fontWeight: "bold",
          mb: 2,
        }}
      >
        Prediction Result
      </Typography>

      <Typography>
        <strong>Prediction:</strong> {result.prediction}
      </Typography>

      <Typography>
        <strong>Model:</strong> {result.model}
      </Typography>

      <Typography>
        <strong>Status:</strong> {result.status}
      </Typography>
    </Paper>
  );
}