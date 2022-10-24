async function handler(event: object, context: object) {
  const gitHubEvent = getGitHubEvent(event);
  const registryEvent = convertToRegistryEvent(gitHubEvent);
  emitRegistryEvent(registryEvent);
}

async function getGitHubEvent(params: type) {}

async function convertToRegistryEvent(params: type) {
  return {
    Entries: [
      {
        Detail: {},
        DetailType: "$registry_action.$github_action",
        EventBusName: "$stageVariables.event_bus",
        TraceHeader: "$allParams.header.x-amzn-trace-id",
      },
    ],
  };
}

async function emitRegistryEvent(registryEvent) {}
