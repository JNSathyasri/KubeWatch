import { useEffect, useState } from "react";
import api from "../api/api";
import Loading from "../components/Loading";

function Pods() {
  const [pods, setPods] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadPods = async () => {
    try {
      const response = await api.get("/pods");
      setPods(response.data.pods);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Unable to fetch pods.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadPods();
    const timer = setInterval(loadPods, 15000);
    return () => clearInterval(timer);
  }, []);

  if (loading) return <Loading />;

  if (error)
    return <div className="alert alert-danger">{error}</div>;

  const filteredPods = pods.filter((pod) =>
    pod.name.toLowerCase().includes(search.toLowerCase())
  );

  const statusBadge = (status) => {
    switch (status) {
      case "Running":
        return <span className="badge bg-success">Running</span>;
      case "Pending":
        return <span className="badge bg-warning text-dark">Pending</span>;
      case "Failed":
        return <span className="badge bg-danger">Failed</span>;
      default:
        return <span className="badge bg-secondary">{status}</span>;
    }
  };

  return (
    <div>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Pods</h2>

        <span className="badge bg-primary fs-6">
          {pods.length} Pods
        </span>

      </div>

      <input
        className="form-control mb-3"
        placeholder="Search Pod..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <div className="card">

        <div className="card-body">

          <div className="table-responsive">

            <table className="table table-hover">

              <thead className="table-dark">

                <tr>

                  <th>Name</th>
                  <th>Namespace</th>
                  <th>Status</th>
                  <th>Ready</th>
                  <th>Restarts</th>
                  <th>Node</th>
                  <th>Pod IP</th>

                </tr>

              </thead>

              <tbody>

                {filteredPods.map((pod) => (

                  <tr key={pod.name}>

                    <td>{pod.name}</td>

                    <td>{pod.namespace}</td>

                    <td>{statusBadge(pod.status)}</td>

                    <td>{pod.ready}</td>

                    <td>{pod.restart_count}</td>

                    <td>{pod.node}</td>

                    <td>{pod.pod_ip}</td>

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

export default Pods;