Name:           python-moddb
Version:        0.8.1
Release:        1
Summary:        A Python scraper/parser for ModDB
License:        MIT
URL:            https://github.com/ClementJ18/moddb
Source0:        https://files.pythonhosted.org/packages/source/m/moddb/moddb-%{version}.tar.gz
Patch:          nonstrict-versioning.patch

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

Requires:       python3dist(pyrate-limiter)
Requires:       python3dist(toolz)

%description
The goal of the library is to be able to navigate ModDB purely programmatically through scraping and parsing of the various models present on the website. 
This is based off a command of my bot which can parse either a game or a mod, this command gave birth to the original library which was extremely limited in its abilities and only able to parse a few pages with inconsistencies. 
This library is a much more mature and professional attempt at the whole idea, adding on a much deeper understanding of OOP.
 
%prep
%autosetup -p1 -n moddb-%{version}

%build
%py_build
 
%install
%py_install

%files
%doc README.md
%{python_sitelib}/moddb-%{version}.dist-info
%{python_sitelib}/moddb/ 
