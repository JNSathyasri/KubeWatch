import { useEffect, useState } from "react";
import api from "../api/api";
import Loading from "../components/Loading";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip
} from "recharts";

function Metrics(){

    const [history,setHistory]=useState([]);

    const [loading,setLoading]=useState(true);

    const [error,setError]=useState("");

    const loadHistory=async()=>{

        try{

            const response=await api.get("/history");

            const formatted=response.data.map(item=>({

                ...item,

                time:new Date(item.timestamp).toLocaleTimeString()

            }));

            setHistory(formatted);

            setError("");

        }

        catch(err){

            console.error(err);

            setError("Unable to load history.");

        }

        finally{

            setLoading(false);

        }

    }

    useEffect(()=>{

        loadHistory();

        const timer=setInterval(loadHistory,30000);

        return ()=>clearInterval(timer);

    },[]);

    if(loading) return <Loading/>

    if(error)
        return(
            <div className="alert alert-danger">
                {error}
            </div>
        )

    return(

        <div>

            <h2 className="mb-4">
                Historical Performance Analytics
            </h2>

            <div className="row">

                <div className="col-lg-6">

                    <div className="chart-container">

                        <h5>
                            CPU Usage History
                        </h5>

                        <ResponsiveContainer
                            width="100%"
                            height={300}
                        >

                            <LineChart data={history}>

                                <CartesianGrid strokeDasharray="3 3"/>

                                <XAxis dataKey="time"/>

                                <YAxis/>

                                <Tooltip/>

                                <Line
                                    type="monotone"
                                    dataKey="cpu_usage"
                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </div>

                </div>

                <div className="col-lg-6">

                    <div className="chart-container">

                        <h5>
                            Memory Usage History
                        </h5>

                        <ResponsiveContainer
                            width="100%"
                            height={300}
                        >

                            <LineChart data={history}>

                                <CartesianGrid strokeDasharray="3 3"/>

                                <XAxis dataKey="time"/>

                                <YAxis/>

                                <Tooltip/>

                                <Line
                                    type="monotone"
                                    dataKey="memory_usage"
                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </div>

                </div>

            </div>

            <div className="card mt-4">

                <div className="card-body">

                    <h5>
                        Historical Metrics
                    </h5>

                    <table className="table table-hover">

                        <thead className="table-dark">

                        <tr>

                            <th>Timestamp</th>

                            <th>CPU (mCPU)</th>

                            <th>Memory (MiB)</th>

                            <th>Pods</th>

                        </tr>

                        </thead>

                        <tbody>

                        {history.map((item,index)=>(

                            <tr key={index}>

                                <td>{item.time}</td>

                                <td>{item.cpu_usage}</td>

                                <td>{item.memory_usage}</td>

                                <td>{item.pods}</td>

                            </tr>

                        ))}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>

    )

}

export default Metrics;