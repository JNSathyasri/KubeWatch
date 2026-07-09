import { useEffect, useState } from "react";
import api from "../api/api";
import Loading from "../components/Loading";

function Services() {

  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadServices = async () => {

    try {

      const response = await api.get("/services");

      setServices(response.data.services);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Unable to fetch services.");

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    loadServices();

    const timer = setInterval(loadServices, 15000);

    return () => clearInterval(timer);

  }, []);

  if (loading) return <Loading />;

  if (error)
    return <div className="alert alert-danger">{error}</div>;

  return (

    <div>

      <div className="d-flex justify-content-between align-items-center mb-4">

        <h2>Services</h2>

        <span className="badge bg-primary fs-6">
          {services.length} Services
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

                  <th>Type</th>

                  <th>Cluster IP</th>

                  <th>Ports</th>

                </tr>

              </thead>

              <tbody>

                {services.map((service) => (

                  <tr key={service.name}>

                    <td>{service.name}</td>

                    <td>{service.namespace}</td>

                    <td>{service.type}</td>

                    <td>{service.cluster_ip}</td>

                    <td>

                      {service.ports.map((port, index) => (

                        <div key={index}>

                          {port.port}/{port.protocol}

                        </div>

                      ))}

                    </td>

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

export default Services;