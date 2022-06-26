const api_url = "http://localhost:8000/posts/?left=0&right=1000000";
const xls_url = "http://localhost:8000/get_xlsx_file/?left=0&right=1000000";
const docx_url = "http://localhost:8000/get_docx_file/?left=0&right=1000000";

export async function get_news_by_filters(filters) {
    let end = ''
    if (filters['category'].length > 0) {
        end += '&search_category=' +  filters['category'];
    }
    if (filters['company_name'].length > 0) {
        end += '&search_company_name=' + filters['company_name'];
    }
    if (filters['resource'].length > 0) {
        end += '&search_resource=' + filters['resource'];
    }
    if (end === '?') {
        end = '';
    }
    return fetch(api_url + end, {})
}

export async function get_archive_by_filters(filters, type) {
    let url = xls_url;
    if (type === 'docx') {
        url = docx_url;
    }
    let end = '';
    if (filters['category'].length > 0) {
        end += '&search_category=' +  filters['category'];
    }
    if (filters['company_name'].length > 0) {
        end += '&search_company_name=' + filters['company_name'];
    }
    if (filters['resource'].length > 0) {
        end += '&search_resource=' + filters['resource'];
    }
    if (end === '?') {
        end = '';
    }
    return fetch(url + end, {})
}