\# Energy Theft / Abnormal Consumption Analytics



\## 1. Project Goal



Build a production-quality IoT analytics platform that analyzes

electricity consumption from multiple virtual smart meters and

identifies abnormal or potentially suspicious consumption patterns.



This is not intended to be a simple demo.



The architecture should allow the virtual meters to later be replaced

with real IoT devices.



\## 2. Core Technology



\- Python

\- MQTT

\- PostgreSQL

\- Grafana

\- Docker

\- REST API

\- Anomaly detection

\- Git



\## 3. Core Data Flow



Virtual Smart Meters

&#x20;       |

&#x20;       v

&#x20;     MQTT

&#x20;       |

&#x20;       v

MQTT Consumer / Ingestion Service

&#x20;       |

&#x20;       v

&#x20;   PostgreSQL

&#x20;       |

&#x20;       +------------------+

&#x20;       |                  |

&#x20;       v                  v

Analytics /             REST API

Anomaly Detection           |

&#x20;       |                   |

&#x20;       v                   v

Anomaly Records         Dashboard / Clients

&#x20;       |

&#x20;       v

&#x20;     Grafana



\## 4. Smart Meter Simulation



The system must support multiple virtual meters.



Each meter should generate realistic electricity consumption data.



The simulator should be able to represent different patterns such as:



\- Normal household consumption

\- Commercial consumption

\- Industrial consumption

\- Peak-hour consumption

\- Low night-time consumption

\- Sudden consumption spikes

\- Sudden consumption drops

\- Repeated abnormal consumption

\- Gradual changes in consumption



The simulator should publish readings through MQTT.



\## 5. MQTT



MQTT will be used as the IoT messaging layer.



The system should support:



\- MQTT broker

\- Publisher

\- Consumer

\- Reconnection

\- Error handling

\- Structured logging

\- JSON payload validation

\- Graceful shutdown



MQTT topic structure should be designed before implementation.



Example concept:



meters/{meter\_id}/readings



The exact topic design should be documented in MQTT\_SPEC.md.



\## 6. Database



PostgreSQL should store:



\- Smart meters

\- Consumption readings

\- Anomaly events

\- Anomaly scores

\- Detection metadata



The database should include:



\- Primary keys

\- Foreign keys

\- Constraints

\- Indexes

\- Timestamps

\- Appropriate data types



Database migrations should be used.



\## 7. Anomaly Detection



The system should detect consumption patterns that differ

significantly from expected behavior.



Initial implementation should support statistical methods such as:



\- Rolling mean

\- Rolling standard deviation

\- Z-score

\- Configurable thresholds



The architecture should allow future models such as:



\- Isolation Forest

\- Local Outlier Factor

\- Other machine-learning models



Anomaly detection should produce an interpretable anomaly score

and relevant metadata.



\## 8. REST API



The backend should expose APIs for:



\- Meters

\- Consumption readings

\- Anomalies

\- Consumption statistics

\- Meter-specific analytics



The exact API specification should be documented separately.



\## 9. Grafana



Grafana should provide dashboards for:



\### Overview



\- Total consumption

\- Number of active meters

\- Number of anomalies

\- Recent suspicious events



\### Consumption



\- Consumption over time

\- Consumption by meter

\- Peak usage

\- Average usage



\### Anomaly Analysis



\- Anomaly events

\- Anomaly scores

\- Suspicious consumption patterns

\- Meter-level anomaly history



\## 10. Testing



The project should contain:



\- Unit tests

\- Integration tests

\- MQTT tests

\- Database tests

\- API tests



Tests should be automated.



\## 11. Reliability



The system should handle:



\- MQTT disconnections

\- Database connection failures

\- Invalid MQTT messages

\- Missing fields

\- Duplicate messages

\- Service restarts



Errors should be logged clearly.



\## 12. Security



Secrets must not be hard-coded.



Configuration should use environment variables.



The project should include:



.env.example



but never commit the actual .env file.



\## 13. Development Principles



The project should:



\- Use modular architecture

\- Follow Python best practices

\- Use type hints where appropriate

\- Include meaningful logging

\- Avoid unnecessary complexity

\- Be testable

\- Be documented

\- Be easy to extend



Do not create a fake implementation merely to make the

dashboard appear functional.



All major components must actually communicate with each other.



\## 14. Development Strategy



Build the project incrementally.



Phase 1:

Architecture and repository setup



Phase 2:

MQTT and smart-meter simulator



Phase 3:

PostgreSQL data layer



Phase 4:

MQTT ingestion service



Phase 5:

Anomaly detection



Phase 6:

REST API



Phase 7:

Grafana dashboards



Phase 8:

Integration testing



Phase 9:

Dockerization and deployment



Phase 10:

Documentation and final validation

