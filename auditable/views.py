from django.shortcuts import render

# Create your views here.

class AuditableMixin(object,):
    def form_valid(self, form, ):
        try:
            if not form.instance.created_by_id :
                form.instance.created_by_id  = self.request.user
                
        except:
            form.instance.created_by_id  = self.request.user
            
        form.instance.modified_by = self.request.user
        return super(AuditableMixin, self).form_valid(form)
