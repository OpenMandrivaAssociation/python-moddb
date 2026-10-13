Name:           python-moddb
Version:        0.15.0
Release:        1
Summary:        A Python scraper/parser for ModDB
License:        MIT
Group:          Development/Python
URL:            https://github.com/ClementJ18/moddb
Source0:        https://files.pythonhosted.org/packages/source/m/moddb/moddb-%{version}.tar.gz
# dropped (no longer applies): Patch:          nonstrict-versioning.patch

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(setuptools)

Requires:       python%{pyver}dist(pyrate-limiter)
Requires:       python%{pyver}dist(toolz)

%description
Scrape and parse ModDB pages so a client can navigate the site
programmatically.
 
%prep
%autosetup -p1 -n moddb-0.15.0

%build
%py_build
 
%install
%py_install

%files
%doc README.md
%{python_sitelib}/moddb-*.egg-info
%{python_sitelib}/moddb/ 
