import { useEffect, useState } from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

import api from "../api/api";
import Loading from "../components/Loading";
import SummaryCard from "../components/SummaryCard";

function Dashboard() {
  const [dashboard, setDashboard] = useState(null);
  const [resources, setResources] = useState(null);
  const [pods, setPods] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadData = async () => {
    try {
      const [dashboardRes, resourcesRes, podsRes] = await Promise.all([
        api.get("/dashboard"),
        api.get("/dashboard/resources"),
        api.get("/dashboard/top-pods"),
      ]);

      setDashboard(dashboardRes.data);
      setResources(resourcesRes.data);
      setPods(podsRes.data);

      setError("");
    } catch (err) {
      console.error(err);
      setError("Unable to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();

    const timer = setInterval(loadData, 15000);

    return () => clearInterval(timer);
  }, []);

  if (loading) return <Loading />;

  if (error)
    return (
      <div className="alert alert-danger">
        {error}
      </div>
    );

  const chartData = [
    {
      name: "CPU",
      value: resources.cpu_usage,
    },
    {
      name: "Memory",
      value: resources.memory_usage,
    },
  ];

  return (
    <div>

      <h2 className="mb-4">
        Cluster Dashboard
      </h2>

      <div className="row">

        <SummaryCard
          title="Nodes"
          value={dashboard.nodes}
          color="#0d6efd"
        />

        <SummaryCard
          title="Pods"
          value={dashboard.pods}
          color="#198754"
        />

        <SummaryCard
          title="Deployments"
          value={dashboard.deployments}
          color="#ffc107"
        />

        <SummaryCard
          title="Services"
          value={dashboard.services}
          color="#dc3545"
        />

      </div>

      <div className="row">

        <div className="col-lg-6 mb-4">

          <div className="chart-container">

            <h5 className="mb-3">
              Live Resource Usage
            </h5>

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <BarChart data={chartData}>

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar dataKey="value" />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>

        <div className="col-lg-6 mb-4">

          <div className="card">

            <div className="card-body">

              <h5>
                Cluster Information
              </h5>

              <table className="table">

                <tbody>

                  <tr>
                    <td>Total Nodes</td>
                    <td>{resources.total_nodes}</td>
                  </tr>

                  <tr>
                    <td>Ready Nodes</td>
                    <td>{resources.ready_nodes}</td>
                  </tr>

                  <tr>
                    <td>Total Pods</td>
                    <td>{resources.total_pods}</td>
                  </tr>

                  <tr>
                    <td>Running Pods</td>
                    <td>{dashboard.running_pods}</td>
                  </tr>

                  <tr>
                    <td>Pending Pods</td>
                    <td>{dashboard.pending_pods}</td>
                  </tr>

                  <tr>
                    <td>Failed Pods</td>
                    <td>{dashboard.failed_pods}</td>
                  </tr>

                  <tr>
                    <td>CPU Usage</td>
                    <td>
                      {resources.cpu_usage} {resources.cpu_unit}
                    </td>
                  </tr>

                  <tr>
                    <td>Memory Usage</td>
                    <td>
                      {resources.memory_usage} {resources.memory_unit}
                    </td>
                  </tr>

                </tbody>

              </table>

            </div>

          </div>

        </div>

      </div>

      <div className="card">

        <div className="card-body">

          <h4 className="mb-4">
            Top Resource Consuming Pods
          </h4>

          <div className="table-responsive">

            <table className="table table-hover">

              <thead className="table-dark">

                <tr>

                  <th>Pod</th>

                  <th>Namespace</th>

                  <th>CPU</th>

                  <th>Memory</th>

                </tr>

              </thead>

              <tbody>

                {pods.map((pod, index) => (

                  <tr key={index}>

                    <td>{pod.name}</td>

                    <td>{pod.namespace}</td>

                    <td>{pod.cpu}</td>

                    <td>{pod.memory}</td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;