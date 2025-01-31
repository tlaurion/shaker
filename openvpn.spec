Name:           3isec-qubes-sys-vpn
Version:       	1.0
Release:        1%{?dist}
Summary:        Salt a VPN proxy in Qubes

License:        GPLv3+
SOURCE0:	openvpn

%description
This package sets up a VPN gateway, named sys-vpn.
It follows the method detailed in the Qubes docs,
 https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md
using iptables and CLI scripts.

The package creates a qube called sys-vpn based on the debian-11-minimal
template.  If the debian-11-minimal template is not present, it will
be downloaded and installed - this may take some time depending on your
net connection.

There are minor changes to the firewall rules on sys-vpn to ensure
blocking of outbound connections.

After installing, copy your openvpn configuration file or zip file
to sys-vpn.
Run setup_vpn to set up the VPN. 
There should be a menu item for this script - if you cannot see it, you may
need to refresh application list in sys-vpn settings.
When finished, restart sys-vpn.

To use the VPN, set sys-vpn as the netvm for your qubes(s).
All traffic will go through the VPN.
The VPN will fail closed if the connection drops.
No traffic will go through clear.

If you remove the package, the salt files will be removed.
**The sys-vpn gateway will also be removed.**
To do this ALL qubes will be checked to see if they use sys-vpn.
If they do, their netvm will be set to `none`.

You can, of course, use template-openvpn to create other VPN gateways.


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/salt
cp -rv %{SOURCE0}/  %{buildroot}/srv/salt

%files
%defattr(-,root,root,-)
/srv/salt/openvpn/*

%post
if [ $1 -eq 1 ]; then
  qubesctl state.apply openvpn.clone
  qubesctl --skip-dom0 --targets=template-openvpn state.apply openvpn.install
  qubesctl state.apply openvpn.create
  qubesctl --skip-dom0 --targets=sys-vpn state.apply openvpn.client_install
fi

%postun
if [ $1 -eq 0 ]; then
  for i in `qvm-ls -O NAME,NETVM | awk '/ sys-vpn/{ print $1 }'`;do qvm-prefs $i netvm none; done
  qvm-kill sys-vpn
  qvm-remove --force sys-vpn template-openvpn 
fi

%changelog
* Wed May 18 2022 unman <unman@thirdeyesecurity.org> - 1.0
- First Build
