import { useEffect, useState } from "react";
import api from "../api/api";
import Loading from "../components/Loading";

function Nodes() {
  const [nodes, setNodes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadNodes = async () => {
    try {
      const response = await api.get("/nodes");
      setNodes(response.data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Unable to fetch node information.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadNodes();

    const interval = setInterval(loadNodes, 15000);

    return () => clearInterval(interval);
  }, []);

  if (loading) return <Loading />;

  if (error)
    return (
      <div className="alert alert-danger">
        {error}
      </div>
    );

  return (
    <div>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Kubernetes Nodes</h2>

        <span className="badge bg-primary fs-6">
          {nodes.length} Node(s)
        </span>

      </div>

      <div className="card">

        <div className="card-body">

          <table className="table table-hover align-middle">

            <thead className="table-dark">

              <tr>

                <th>Name</th>

                <th>Operating System</th>

                <th>Kubernetes Version</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              {nodes.map((node, index) => (

                <tr key={index}>

                  <td>

                    <strong>{node.name}</strong>

                  </td>

                  <td>{node.os}</td>

                  <td>{node.kubelet_version}</td>

                  <td>

                    {node.ready === "True" ? (

                      <span className="badge bg-success">

                        Ready

                      </span>

                    ) : (

                      <span className="badge bg-danger">

                        Not Ready

                      </span>

                    )}

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}

export default Nodes;