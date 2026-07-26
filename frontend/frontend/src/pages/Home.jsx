import { Box, Container } from "@mui/material";
import AppHeader from "../components/AppHeader";
import PredictionForm from "../components/PredictionForm";

export default function Home() {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        backgroundColor: "#000",
        color: "#fff",
      }}
    >
      <AppHeader />

      <Container maxWidth="md" sx={{ py: 5 }}>
        <PredictionForm />
      </Container>
    </Box>
  );
}