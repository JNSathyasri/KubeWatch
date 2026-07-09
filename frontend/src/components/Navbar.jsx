function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg bg-white shadow-sm px-4">

      <div className="container-fluid">

        <span className="navbar-brand fw-bold fs-4">
          KubeWatch
        </span>

        <div className="ms-auto">

          <span className="badge bg-success fs-6">
            Kubernetes Monitoring
          </span>

        </div>

      </div>

    </nav>
  );
}

export default Navbar;