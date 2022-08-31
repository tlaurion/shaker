qvm-present-id:
  qvm.present:
    - name: sys-whonix
    - template: whonix-gw-16
    - label: gray

qvm-prefs-id:
  qvm.prefs:
    - name: sys-whonix
    - memory: 300
    - maxmem: 800
    - vcpus: 2
    - provides-network: true

qvm-features-id:
  qvm.features:
    - name: sys-whonix
    - disable:
      - service.cups
      - service.cups-browsed
      - service.tinyproxy

'qvm-volume extend sys-whonix:private 20G' :
  cmd.run
