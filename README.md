# codex-issue-agent

An automated GitHub agent that uses OpenAI Codex to automatically handle issue assignments and PR review changes.

## Features

- **Automatic Issue Processing**: When an issue is assigned to the configured user, the agent automatically:
  - Creates a branch from the issue
  - Uses OpenAI Codex to implement the solution
  - Generates an AI-powered commit message
  - Creates a pull request with an AI-generated description

- **Automatic PR Review Response**: When changes are requested on a PR, the agent:
  - Automatically applies the requested changes using OpenAI Codex
  - Commits and pushes the updates

## How to Use This Agent

To integrate this agent into your own repository, follow these steps:

### 1. Copy the Workflows Folder

Copy the `.github/workflows` folder from this repository to your repository:

```bash
# Clone this repository
git clone https://github.com/vseichter/codex-issue-agent.git

# Copy the workflows folder to your repository
cp -r codex-issue-agent/.github/workflows /path/to/your/repo/.github/
```

The folder contains two workflow files:
- `issue-assigned.yml` - Handles automatic issue processing
- `pr-changes-requested.yml` - Handles automatic PR review changes

### 2. Configure Required Secrets

The workflows require the following secrets to be configured in your repository:

#### GitHub Personal Access Token (PAT)

Create a Personal Access Token with the following permissions:
- `repo` (Full control of private repositories)
- `workflow` (Update GitHub Action workflows)

**How to create a GitHub PAT:**
1. Go to [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token" > "Generate new token (classic)"
3. Give your token a descriptive name (e.g., "Codex Issue Agent")
4. Select the required scopes: `repo` and `workflow`
5. Click "Generate token"
6. Copy the token immediately (you won't be able to see it again)

**Add the PAT to your repository:**
1. Go to your repository on GitHub
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `PAT`
5. Value: Paste your Personal Access Token
6. Click "Add secret"

**Official GitHub documentation:**
- [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)

#### OpenAI API Key

The agent uses OpenAI's API for Codex CLI and GPT models. You'll need an OpenAI API key.

**How to get an OpenAI API key:**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to [API Keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Give your key a name and click "Create secret key"
6. Copy the API key immediately (you won't be able to see it again)

**Add the OpenAI API key to your repository:**
1. Go to your repository on GitHub
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `open_api_key` (note: both workflows use this name)
5. Value: Paste your OpenAI API key
6. Click "Add secret"

**Optional:** You can also add `OPENAI_API_KEY` as an additional secret name for compatibility.

**Official OpenAI documentation:**
- [OpenAI API Keys](https://platform.openai.com/docs/quickstart/account-setup)

### 3. Configure Workflow Permissions

The workflows require the following permissions:
- `contents: write` - To create branches and commit changes
- `issues: write` - To interact with issues
- `pull-requests: write` - To create and update pull requests

These permissions are already configured in the workflow files using the `permissions` key.

### 4. Customize the Workflow (Optional)

By default, the `issue-assigned.yml` workflow only triggers when issues are assigned to the user `vseichter`. To change this:

1. Edit `.github/workflows/issue-assigned.yml`
2. Find line 14: `if: ${{ github.event.assignee.login == 'vseichter' }}`
3. Replace `'vseichter'` with your GitHub username

Example:
```yaml
if: ${{ github.event.assignee.login == 'yourusername' }}
```

### 5. Dependencies

The workflows automatically install the following dependencies:
- **Node.js** (>=20) - Installed via `actions/setup-node@v3`
- **OpenAI Codex CLI** - Installed via `npm install -g @openai/codex`
- **GitHub CLI tools** - Pre-installed in GitHub Actions runners

No manual installation is required; the workflows handle all dependencies automatically.

## How It Works

1. **Issue Assignment Trigger**: When you assign an issue to yourself (or the configured user), the `issue-assigned.yml` workflow automatically triggers.

2. **Branch Creation**: The workflow creates a branch named `issue-{number}-{sanitized-title}`.

3. **AI Code Generation**: The OpenAI Codex CLI analyzes the issue title and body, then generates code changes to address the issue.

4. **Automated Commit**: Changes are committed with an AI-generated commit message.

5. **PR Creation**: A pull request is automatically created with an AI-generated description.

6. **Review Response**: If a reviewer requests changes, the `pr-changes-requested.yml` workflow automatically applies those changes and commits them.

## Requirements

- GitHub repository with Actions enabled
- OpenAI API account with available credits
- GitHub Personal Access Token
- Node.js >=20 (automatically installed by the workflow)

## License

See [LICENSE](LICENSE) file for details.