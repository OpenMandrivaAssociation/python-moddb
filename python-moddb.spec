Name:           python-moddb
Version:        0.15.0
Release:        1
Summary:        A Python scraper/parser for ModDB
License:        MIT
Group:          Development/Python
URL:            https://github.com/ClementJ18/moddb
Source0:        https://files.pythonhosted.org/packages/source/m/moddb/moddb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(setuptools)
# setup.py imports packaging to parse requirements.txt
BuildRequires:  python%{pyver}dist(packaging)
# boxes.py imports typing_extensions. Upstream does not declare it.
Requires:       python%{pyver}dist(typing-extensions)

%description
Scrape and parse ModDB pages.

%prep
%autosetup -p1 -n moddb-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
# setup.py install writes egg-info, not a wheel dist-info
%{python_sitelib}/moddb-%{version}-py%{pyver}.egg-info
%{python_sitelib}/moddb/
