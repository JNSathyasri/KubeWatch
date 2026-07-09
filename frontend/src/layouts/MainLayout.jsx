import { Outlet } from "react-router-dom";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

function MainLayout() {
  return (
    <div className="wrapper">

      <Sidebar />

      <div className="content">

        <Navbar />

        <div className="page-content">

          <Outlet />

        </div>

      </div>

    </div>
  );
}

export default MainLayout;