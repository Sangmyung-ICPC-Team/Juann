/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* create_node(int val)
{
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

struct TreeNode* insertIntoBST(struct TreeNode* root, int val){

    if(!root)
        return create_node(val);
    if(root->val < val)
        root->right = insertIntoBST(root->right, val);
    else if(root->val > val)
        root->left = insertIntoBST(root->left, val);
    
    return root;
}
