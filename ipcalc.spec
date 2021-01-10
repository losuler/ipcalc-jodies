%global sha512 089eb2b9a38b07caa182ff11547a93d86aed570311fc8cd9e636c7546ab4d15acc854b9d79bbba9c797dcfbbedd1d6f4d521aec97bf613905fe5198a29c9889d

Name:           ipcalc-jodies
Version:        0.41
Release:        4%{?dist}
Summary:        IPv4 Address Calculator

License:        GPLv2
URL:            http://jodies.de/ipcalc
Source0:        http://jodies.de/ipcalc-archive/ipcalc-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: coreutils

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving a
second netmask, you can design subnets and supernets. It is also
presents the subnetting results as easy-to-understand binary values.

Enter your netmask(s) in CIDR notation (/25) or dotted decimals
(255.255.255.0). Inverse netmasks are recognized. If you omit the
netmask ipcalc uses the default netmask for the class of your network.

%prep
echo -n ${sha512} ipcalc-%{version}.tar.gz | sha512sum -c -
%autosetup -n ipcalc-%{version}

%install
install -Dm0755 ipcalc %{buildroot}%{_bindir}/%{name}

%files
%license license
%doc changelog contributors
%{_bindir}/%{name}

%changelog
* Sun Jan 10 2021 losuler <losuler@posteo.net> - 0.41-4
- Add source file hash verification

* Wed Aug 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.41-3
- Initial package

