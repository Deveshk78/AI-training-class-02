public class ModelClient {
    private final String provider;
    private final String modelName;

    public ModelClient(String provider, String modelName) {
        this.provider = provider;
        this.modelName = modelName;
    }

    public String generateResponse(String prompt) {
        if ("mock".equalsIgnoreCase(provider)) {
            return "[Mock Java] Response for: " + prompt.substring(0, Math.min(prompt.length(), 80));
        }
        return "[Live provider: " + provider + "] Response for: " + prompt;
    }

    public String getModelName() {
        return modelName;
    }
}
