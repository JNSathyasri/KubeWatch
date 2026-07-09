import { NavLink } from "react-router-dom";

function Sidebar() {
  return (
    <div className="sidebar text-white p-3">

      <h3 className="mb-4 text-center">
        KubeWatch
      </h3>

      <div className="nav flex-column">

        <NavLink
          className="nav-link"
          to="/dashboard"
        >
          Dashboard
        </NavLink>

        <NavLink
          className="nav-link"
          to="/nodes"
        >
          Nodes
        </NavLink>

        <NavLink
          className="nav-link"
          to="/pods"
        >
          Pods
        </NavLink>

        <NavLink
          className="nav-link"
          to="/deployments"
        >
          Deployments
        </NavLink>

        <NavLink
          className="nav-link"
          to="/services"
        >
          Services
        </NavLink>

        <NavLink
          className="nav-link"
          to="/metrics"
        >
          Metrics
        </NavLink>

        <NavLink
          className="nav-link"
          to="/logs"
        >
          Logs
        </NavLink>

      </div>
    </div>
  );
}

export default Sidebar;