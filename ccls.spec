Name:           ccls
Version:        0.20210330
Release:        1%{?dist}
Summary:        C/C++/ObjC language server

# main package is Apache 2.0
# bundled dependencies are Boost (macro_map) and CC0 (siphash)
License:        ASL 2.0 and CC0 and Boost
URL:            https://github.com/MaskRay/ccls
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.8
BuildRequires:  gcc-c++ >= 7.2
BuildRequires:  llvm-devel >= 7.0
BuildRequires:  clang-devel >= 7.0
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel

Requires:       llvm >= 7.0

Provides:       bundled(siphash)
Provides:       bundled(macro_map)

%description
ccls, which originates from cquery, is a C/C++/Objective-C language server.

- code completion (with both signature help and snippets)
- definition/references, and other cross references
- cross reference extensions: $ccls/call $ccls/inheritance $ccls/member
  $ccls/vars ...
- formatting
- hierarchies: call (caller/callee) hierarchy, inheritance (base/derived)
  hierarchy, member hierarchy
- symbol rename
- document symbols and approximate search of workspace symbol
- hover information
- diagnostics and code actions (clang FixIts)
- semantic highlighting and preprocessor skipped regions
- semantic navigation: $ccls/navigate


%prep
%autosetup
rm -rf third_party/rapidjson

%build
mkdir build && pushd build
%cmake ..

%make_build
popd

%install
%make_install -C build

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Sun Jan 20 2022 Philippe Normand <philn@igalia.com> - 0.20210330-1
- Initial import from un-maintained spec file.

* Sun Mar 15 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.5-2
- Fix dependency on the current clang version (fix for rhbz#1807574)

* Tue Nov 12 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.5-1
- New upstream release 20190823.5

* Sun Oct 27 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.4-1
- New upstream release 20190823.4

* Mon Sep 30 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.3-1
- New upstream release 20190823.3

* Sun Sep 29 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.2-1
- New upstream release 20190823.2

* Sat Sep  7 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.1-1
- New upstream release 20190823.1

* Sat Aug 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823-1
- New upstraem release 20190823

* Sun Mar 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190314-1
- Bump version to the Pi Day Release

* Thu Mar  7 2019 Dan Čermák <dcermak@suse.com> - 0.20181225.8-1
- Initial package version for Fedora & openSUSE
