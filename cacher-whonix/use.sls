qvm-present-id:
  qvm.present:
    - name: cacher
    - template: whonix-gw-16
    - label: gray

/etc/qubes/policy.d/30-user.policy:
  file.prepend:
    - text:
      - "qubes.UpdatesProxy  *  @tag:whonix-updatevm  @default  allow target=sys-whonix"
      - "qubes.UpdatesProxy  *  @tag:whonix-updatevm  @anyvm    deny"
      - "qubes.UpdatesProxy  *  @type:TemplateVM      @default  allow target=sys-whonix"
