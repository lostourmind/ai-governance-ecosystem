# Flask API Node Supplement

```yaml
node_context:
  path: "project.coding.python.flask_api"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- **Environment Configuration**: Use os.getenv() or python-dotenv for all secrets and configuration
- **Input Validation**: Implement schema validation using marshmallow or pydantic
- **Authentication**: Use flask-login or JWT with proper token management
- **Database**: Use SQLAlchemy ORM with connection pooling
- **Error Handling**: Return structured errors without exposing internal details

### Domain-Specific Knowledge
**Critical Success Factors:**
- Environment-based configuration management prevents credential exposure
- Input validation prevents injection attacks and data corruption
- Proper authentication middleware secures all protected endpoints
- Database connection pooling optimizes performance and resource usage

**Known Pitfalls:**
- Debug mode enabled in production exposes sensitive debugging information
- Missing input validation leads to injection vulnerabilities
- Hardcoded secrets create security risks and deployment complications
- Inadequate error handling exposes internal system details to attackers

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - environment_variables_used_for_configuration
    - input_validation_schemas_present
    - authentication_middleware_implemented
    - structured_error_handling_configured
  quality_gates:
    - no_hardcoded_credentials_in_code
    - all_endpoints_properly_protected
    - database_queries_use_orm_parameters
    - cors_configured_appropriately
  success_criteria:
    - api_endpoints_respond_with_proper_status_codes
    - authentication_flow_works_end_to_end
    - database_operations_handle_errors_gracefully
    - input_validation_rejects_malformed_requests
```

### Integration Guidance
**Compatible Approaches:**
- Flask-RESTful for structured API development
- SQLAlchemy with Alembic for database migrations
- Marshmallow for request/response serialization
- Flask-CORS for cross-origin request handling

**Incompatible Patterns:**
- Raw SQL queries with string concatenation (injection risk)
- Session storage without proper security measures
- Missing input validation (security vulnerability)
- Exposing debug information in production responses
