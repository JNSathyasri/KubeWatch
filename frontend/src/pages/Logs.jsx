import { useState } from "react";
import api from "../api/api";

function Logs(){

    const [namespace,setNamespace]=useState("");

    const [pod,setPod]=useState("");

    const [logs,setLogs]=useState("");

    const [error,setError]=useState("");

    const fetchLogs=async()=>{

        if(!namespace||!pod){

            alert("Enter namespace and pod.");

            return;

        }

        try{

            const response=await api.get(`/logs/${namespace}/${pod}`);

            setLogs(response.data.logs || JSON.stringify(response.data,null,2));

            setError("");

        }

        catch(err){

            console.error(err);

            setError("Unable to fetch logs.");

        }

    }

    return(

        <div>

            <h2 className="mb-4">
                Pod Logs
            </h2>

            {error &&
                <div className="alert alert-danger">
                    {error}
                </div>
            }

            <div className="card">

                <div className="card-body">

                    <div className="row">

                        <div className="col-md-5">

                            <input

                            className="form-control"

                            placeholder="Namespace"

                            value={namespace}

                            onChange={(e)=>setNamespace(e.target.value)}

                            />

                        </div>

                        <div className="col-md-5">

                            <input

                            className="form-control"

                            placeholder="Pod Name"

                            value={pod}

                            onChange={(e)=>setPod(e.target.value)}

                            />

                        </div>

                        <div className="col-md-2">

                            <button

                            className="btn btn-primary w-100"

                            onClick={fetchLogs}

                            >

                            Fetch

                            </button>

                        </div>

                    </div>

                </div>

            </div>

            <div className="card mt-4">

                <div className="card-body">

                    <pre
                    style={{
                        whiteSpace:"pre-wrap",
                        maxHeight:"600px",
                        overflow:"auto"
                    }}
                    >
                        {logs}
                    </pre>

                </div>

            </div>

        </div>

    )

}

export default Logs;