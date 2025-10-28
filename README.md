# NixLine Demo2 - Configuration-Driven Consumer

This repository demonstrates advanced NixLine configuration using `.nixline.toml` for comprehensive customization without forking the NixLine baseline repository.

## Key Features Demonstrated

**Organization Customization**
- Custom organization name (AcmeCorp)
- Organization-specific email addresses
- Team structure and ownership rules

**Selective Pack Adoption**
- Choose which policies to adopt (editorconfig, codeowners, security, license and precommit)
- Exclude unwanted packs (dependabot intentionally excluded)

**Pack Parameterization**
- EditorConfig: Custom indentation (2 spaces), line length (80) and language-specific rules
- CODEOWNERS: Multi-team ownership structure reflecting AcmeCorp's organization
- Security: Custom response times, coordinated disclosure and version support matrix
- License: MIT license with custom holder and year

**Direct Consumption Pattern**
- No local flake.nix maintenance required
- Configuration-driven policy materialization using enhanced sync app
- Runtime configuration passing to parameterized packs
- Custom file support for complete content override
- Instant updates from NixLine baseline with local customization

## Quick Start

View Current Configuration:
```bash
cat .nixline.toml
```

Sync Policies (Enhanced Version):
```bash
# Sync with configuration file
nix run github:NixLine-org/nixline-baseline#sync

# Preview changes without applying
nix run github:NixLine-org/nixline-baseline#sync -- --dry-run

# Override specific values
nix run github:NixLine-org/nixline-baseline#sync -- --override org.name=MyCompany

# Use custom config file
nix run github:NixLine-org/nixline-baseline#sync -- --config my-config.toml
```

Validate Policies:
```bash
nix run github:NixLine-org/nixline-baseline#check
```

## Configuration Highlights

Organization Structure:
```toml
[organization]
name = "AcmeCorp"
security_email = "security@acme.com"
default_team = "@AcmeCorp/maintainers"
```

Custom EditorConfig:
```toml
[packs.editorconfig]
indent_size = 2
line_length = 80

[packs.editorconfig.languages]
python = { indent_size = 4, max_line_length = 88 }
```

Multi-Team Code Ownership:
```toml
[packs.codeowners]
rules = [
  { pattern = "*.py", owners = ["@AcmeCorp/python-team"] },
  { pattern = "*.{js,jsx,ts,tsx}", owners = ["@AcmeCorp/frontend-team"] },
  { pattern = "docs/**", owners = ["@AcmeCorp/docs-team"] }
]
```

## Generated Policy Files

After running sync, the following files are materialized:

| File | Customization |
|------|---------------|
| .editorconfig | 2-space indentation, 80-char line length and language-specific rules |
| .github/CODEOWNERS | AcmeCorp teams and multi-language ownership rules |
| SECURITY.md | AcmeCorp contact, 2-day response time and version matrix |
| LICENSE | MIT license with AcmeCorp as holder |
| .pre-commit-config.yaml | Python + JavaScript toolchain with custom settings |

## Comparison: Demo1 vs Demo2

| Feature | Demo1 (Basic) | Demo2 (Advanced) |
|---------|---------------|------------------|
| Customization | Pack selection only | Full parameterization |
| Organization | Uses NixLine defaults | Custom AcmeCorp branding |
| Configuration | CLI arguments only | TOML configuration file |
| Code ownership | Generic rules | Multi-team structure |
| Flexibility | Limited | Extensive customization |

## Architectural Benefits

**Zero Fork Maintenance**
No need to fork and maintain the NixLine baseline repository. Automatic updates from the upstream NixLine baseline with local customization preserved. Configuration-driven policy inheritance.

**Scalable Governance**
One .nixline.toml file controls all policies. Consistent customization across all repositories. Easy to replicate across organization.

**Developer Experience**
Self-documenting configuration. Preview changes with --dry-run. Override any setting via CLI. Complete file override capability with custom_file.

**Organization Alignment**
Policies reflect actual team structure. Custom response times and contacts. Language-specific tooling configuration. Selective policy adoption.

## Advanced Usage Examples

Environment-Specific Overrides:
```bash
# Development environment with relaxed policies
nix run .#sync -- --override packs.security.response_time="within 1 week"

# Production environment with strict settings
nix run .#sync -- --override packs.editorconfig.line_length=100
```

Multi-Repository Consistency:
```bash
# Use same config across multiple repos
cp .nixline.toml ../other-acme-repo/
cd ../other-acme-repo && nix run github:NixLine-org/nixline-baseline#sync
```

Custom File Override (Example):
```bash
# Create custom license file
echo "Proprietary License for AcmeCorp" > my-license.txt

# Update config to use custom file
# [packs.license]
# custom_file = "my-license.txt"

# Sync to apply custom license
nix run github:NixLine-org/nixline-baseline#sync
```

## Why This Architecture Matters

This approach solves the organizational governance fork problem:

Traditional Approach: Every organization forks their own governance repository. Result: 100 organizations = 100 divergent governance repositories that become outdated.

NixLine Approach: One centrally maintained NixLine baseline repository + organization-specific configuration files. Result: 100 organizations = 1 shared baseline + 100 config files.

Improvements to the shared NixLine baseline repository benefit all organizations automatically, while each organization maintains full customization control through their configuration files.
