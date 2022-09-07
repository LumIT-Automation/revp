Name:       automation-interface-reverse-proxy-container
Version:    RH_VERSION
Release:    RH_RELEASE
Summary:    Automation Interface Reverse Proxy, container image

License:    GPLv3+
Source0:    RPM_SOURCE

Requires:   podman, buildah, at, cronie
Requires:   automation-interface-log >= 1.2

BuildArch:  x86_64

%description
automation-interface-reverse-proxy-container

%include %{_topdir}/SPECS/preinst.spec
%include %{_topdir}/SPECS/postinst.spec
%include %{_topdir}/SPECS/prerm.spec
%include %{_topdir}/SPECS/postrm.spec

%prep
%setup  -q #unpack tarball

%install
cp -rfa * %{buildroot}

%include %{_topdir}/SPECS/files.spec



