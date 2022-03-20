# Importing the required modules
from pagaya_learn.pagaya_learn.workflow.workflow_compiler import WorkflowCompiler
from pglearn_devkit.assets import AssetsDownloader, DateTimeRange
from pglearn_devkit.policies.clients.github import GithubPoliciesClient
from pglearn_devkit.runner import run_pipeline
from rich import print

# Init gh client
client = GithubPoliciesClient.load_default()

# Let's get the list of all the policies currently available in prduction
policy = client.get_policies("master").get("avant/policies/AVANT_EP_20201004")

# Init assets client
assets = AssetsDownloader()

# Then we can list the versions available to download.
print(f" Resources Versions:{assets.resources.list_versions()}")

# Once we found the version that we want to download, you can download it easily.
resources = assets.resources.download("0.1.8")

# Time to download apps. simply choose a platform and a time-range in which to search for applications
raw_apps = assets.chitom_artifacts.download_for_platform(
    "avant",
    DateTimeRange.from_hours_ago(99999),
    limit=4,
).applications

# Here you can already see the raw applications that chitom received.
print(f"Got {len(raw_apps.raw_applications)} raw apps!")

# Now we can start the process of building a pipeline
pipeline = WorkflowCompiler(*resources).compile(policy)

# Now that we got a pipeline - We can fill the missing inputs
apps = raw_apps.prepare(pipeline)

# Done with that. Run the pipeline!
results = run_pipeline(pipeline, apps.df)
print(results)
