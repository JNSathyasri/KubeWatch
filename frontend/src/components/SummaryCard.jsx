function SummaryCard({ title, value, color }) {

    return (

        <div className="col-lg-3 col-md-6 mb-4">

            <div className="card">

                <div className="card-body">

                    <h6 className="summary-title">
                        {title}
                    </h6>

                    <h2
                        className="summary-number"
                        style={{ color }}
                    >
                        {value}
                    </h2>

                </div>

            </div>

        </div>

    );

}

export default SummaryCard;