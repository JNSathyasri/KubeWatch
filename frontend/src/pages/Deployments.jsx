import { useEffect, useState } from "react";
import api from "../api/api";
import Loading from "../components/Loading";

function Deployments() {
  const [deployments, setDeployments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadDeployments = async () => {
    try {
      const response = await api.get("/deployments");
      setDeployments(response.data.deployments);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Unable to fetch deployments.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDeployments();
    const timer = setInterval(loadDeployments, 15000);
    return () => clearInterval(timer);
  }, []);

  if (loading) return <Loading />;

  if (error)
    return <div className="alert alert-danger">{error}</div>;

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Deployments</h2>

        <span className="badge bg-primary fs-6">
          {deployments.length} Deployments
        </span>
      </div>

      <div className="card">
        <div className="card-body">

          <div className="table-responsive">

            <table className="table table-hover">

              <thead className="table-dark">

                <tr>
                  <th>Name</th>
                  <th>Namespace</th>
                  <th>Ready</th>
                  <th>Available</th>
                  <th>Desired</th>
                  <th>Strategy</th>
                </tr>

              </thead>

              <tbody>

                {deployments.map((deployment) => (

                  <tr key={deployment.name}>

                    <td>{deployment.name}</td>

                    <td>{deployment.namespace}</td>

                    <td>
                      {deployment.ready_replicas}/
                      {deployment.desired_replicas}
                    </td>

                    <td>{deployment.available_replicas}</td>

                    <td>{deployment.desired_replicas}</td>

                    <td>{deployment.strategy}</td>

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

export default Deployments;