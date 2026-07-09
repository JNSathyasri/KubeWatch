import { Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Dashboard from "./pages/Dashboard";
import Nodes from "./pages/Nodes";
import Pods from "./pages/Pods";
import Deployments from "./pages/Deployments";
import Services from "./pages/Services";
import Metrics from "./pages/Metrics";
import Logs from "./pages/Logs";

function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout />}>
        <Route index element={<Navigate to="/dashboard" replace />} />

        <Route path="dashboard" element={<Dashboard />} />
        <Route path="nodes" element={<Nodes />} />
        <Route path="pods" element={<Pods />} />
        <Route path="deployments" element={<Deployments />} />
        <Route path="services" element={<Services />} />
        <Route path="metrics" element={<Metrics />} />
        <Route path="logs" element={<Logs />} />
      </Route>
    </Routes>
  );
}

export default App;